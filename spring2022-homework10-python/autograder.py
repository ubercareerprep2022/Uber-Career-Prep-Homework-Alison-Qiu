# Firstname Lastname
# NetID
# COMP 182 Spring 2021 - Homework 8, Problem 2

# You may NOT import anything apart from already imported libraries.
# You can use helper functions from provided.py, but they have
# to be copied over here.


import math
import random
import numpy
from collections import *


#################   PASTE PROVIDED CODE HERE AS NEEDED   #################

class HMM:
    """
    Simple class to represent a Hidden Markov Model.
    """
    def __init__(self, order, initial_distribution, emission_matrix, transition_matrix):
        self.order = order
        self.initial_distribution = initial_distribution
        self.emission_matrix = emission_matrix
        self.transition_matrix = transition_matrix

def read_pos_file(filename):
    """
    Parses an input tagged text file.
    Input:
    filename --- the file to parse
    Returns:
    The file represented as a list of tuples, where each tuple
    is of the form (word, POS-tag).
    A list of unique words found in the file.
    A list of unique POS tags found in the file.
    """
    file_representation = []
    unique_words = set()
    unique_tags = set()
    f = open(str(filename), "r")
    for line in f:
        if len(line) < 2 or len(line.split("/")) != 2:
            continue
        word = line.split("/")[0].replace(" ", "").replace("\t", "").strip()
        tag = line.split("/")[1].replace(" ", "").replace("\t", "").strip()
        file_representation.append( (word, tag) )
        unique_words.add(word)
        unique_tags.add(tag)
    f.close()
    return file_representation, unique_words, unique_tags


def bigram_viterbi(hmm, sentence):
    """
    Run the Viterbi algorithm to tag a sentence assuming a bigram HMM model.
    Inputs:
      hmm --- the HMM to use to predict the POS of the words in the sentence.
      sentence ---  a list of words.
    Returns:
      A list of tuples where each tuple contains a word in the
      sentence and its predicted corresponding POS.
    """

    # Initialization
    viterbi = defaultdict(lambda: defaultdict(int))
    backpointer = defaultdict(lambda: defaultdict(int))
    unique_tags = set(hmm.initial_distribution.keys()).union(set(hmm.transition_matrix.keys()))
    for tag in unique_tags:
        if (hmm.initial_distribution[tag] != 0) and (hmm.emission_matrix[tag][sentence[0]] != 0):
            viterbi[tag][0] = math.log(hmm.initial_distribution[tag]) + math.log(hmm.emission_matrix[tag][sentence[0]])
            #print('for tag ',tag, ' math.log(hmm.initial_distribution[tag]) ',  hmm.initial_distribution[tag],'math.log(hmm.emission_matrix[tag][sentence[0]]) ',hmm.emission_matrix[tag][sentence[0]])
        else:
            viterbi[tag][0] = -1 * float('inf')
        #print('for tag ',tag, 'viterbi[tag][0] is ',viterbi[tag][0] )

    # Dynamic programming.
    for t in range(1, len(sentence)):
        backpointer["No_Path"][t] = "No_Path"
        for s in unique_tags:
            max_value = -1 * float('inf')
            max_state = None
            for s_prime in unique_tags:
                #print('transition from tag ',s_prime, ' to ',s)
                #v[l',i-1]
                val1= viterbi[s_prime][t-1]
               #Al',l
                val2 = -1 * float('inf')
                if hmm.transition_matrix[s_prime][s] != 0:
                    val2 = math.log(hmm.transition_matrix[s_prime][s])
                #print("val1, val2, ",val1, val2)
                curr_value = val1 + val2
                if curr_value > max_value:
                    #print('!!!curr_value > max_value:')
                    max_value = curr_value
                    max_state = s_prime
                #print('max_state: ',max_state,'max_value ',max_value)

             #El(xi)
            val3 = -1 * float('inf')
            if hmm.emission_matrix[s][sentence[t]] != 0:
                val3 = math.log(hmm.emission_matrix[s][sentence[t]])
            viterbi[s][t] = max_value + val3
            #print('-------backpointer')
            if max_state == None:
                backpointer[s][t] = "No_Path"
            else:
                backpointer[s][t] = max_state
                #print('backpointer',s,t,' is ',backpointer[s][t])
    for ut in unique_tags:
        string = ""
        for i in range(0, len(sentence)):
            if (viterbi[ut][i] != float("-inf")):
                string += str(int(viterbi[ut][i])) + "\t"
            else:
                string += str(viterbi[ut][i]) + "\t"
    #print('string: ',string)
    # Termination
    max_value = -1 * float('inf')
    last_state = None
    final_time = len(sentence) -1
    for s_prime in unique_tags:
        #print('viterbi of ', s_prime,final_time, 'is ',viterbi[s_prime][final_time])
        if viterbi[s_prime][final_time] > max_value:
            max_value = viterbi[s_prime][final_time]
            last_state = s_prime
    if last_state == None:
        last_state = "No_Path"
    # print('last_state',last_state)
    # print('viterbi, ',viterbi)
    # print('backpointer',backpointer)
    # Traceback
    tagged_sentence = []
    tagged_sentence.append((sentence[len(sentence)-1], last_state))
    for i in range(len(sentence)-2, -1, -1):
        next_tag = tagged_sentence[-1][1]
        curr_tag = backpointer[next_tag][i+1]
        #print('next_tag ',next_tag,'curr_tag ',curr_tag)
        tagged_sentence.append((sentence[i], curr_tag))
    tagged_sentence.reverse()
    return tagged_sentence


#####################  STUDENT CODE BELOW THIS LINE  #####################

def compute_counts(training_data: list, order: int) -> tuple:
    """
	input 
	- a list of (word, POS-tag) pairs returned by the function read_pos_file, 
	- the order of the HMM.

	output: 
	- If order equals 2, the function returns a tuple containing 
	the number of tokens in training_data, 
	a dictionary that contains that contains  
	C ( t i , w i )  for every unique tag and unique word (keys correspond 
	to tags), 
	a dictionary that contains  C ( t i )  as above, 
	and a dictionary that contains  C ( t i − 1 , t i )  as above, in this order. 
	
	If order equals 3, the function returns as the fifth element 
	a dictionary that contains  C ( t i − 2 , t i − 1 , t i ) ,
	in addition to the other four elements.
	"""
    tokens = len(training_data)
    c_ti_wi = defaultdict(lambda: defaultdict(int))
    c_ti = defaultdict(int)
    c_timinus1_ti = defaultdict(lambda: defaultdict(int))
    if order == 2:
        prev_tag = None
        for tuple in training_data:
            word = tuple[0] #'The'
            tag = tuple[1] #'DT'
            c_ti_wi[tag][word] +=1
            c_ti[tag] += 1
            if prev_tag is not None:
                c_timinus1_ti[prev_tag][tag] += 1
            prev_tag = tag
    if order == 3:
        c_timinus2_timinus1_ti = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
            
        prev_tag = None
        prev_prev_tag = None
        for tuple in training_data: 
            word = tuple[0] #'The'
            tag = tuple[1] #'DT'
            c_ti_wi[tag][word] +=1
            c_ti[tag] += 1
            if prev_tag is not None:
                c_timinus1_ti[prev_tag][tag] += 1
            temp, prev_tag = prev_tag, tag
            if prev_prev_tag is not None:
                c_timinus2_timinus1_ti[prev_prev_tag][temp][tag] +=1
                #print('c_timinus2_timinus1_ti: ',c_timinus2_timinus1_ti)  
            prev_prev_tag = temp      
    return (tokens,c_ti_wi,c_ti,c_timinus1_ti,c_timinus2_timinus1_ti) if order ==3 else (tokens,c_ti_wi,c_ti,c_timinus1_ti)


def compute_initial_distribution(training_data: list, order: int) -> dict:
    """
	input:
		- a list of (word, POS-tag) pairs returned by the function read_pos_file, 
		- the order of the HMM.
	output:
		- a dictionary that contains π^1 if order equals 2, and π^2 if order equals 3.
	"""
    
    total_sentences = 1
    if order == 2:
        #initialize 1d and 2d disctionaries
        pi = defaultdict(int)
        #the first tag in training data
        pi[training_data[0][1]]+=1

        #loop through tuples
        for index in range(1,len(training_data)-1):
            #find the periods
            if training_data[index][1]=='.':
                total_sentences +=1
                #if order = 2, add one to the count of tag that comes after "."
                pi[training_data[index+1][1]]+=1
        #normalize so that total probability is 1
        for key in pi:
            pi[key]=pi[key]/total_sentences
    if order == 3:
        #initialize 1d and 2d disctionaries
        pi = defaultdict(lambda: defaultdict(int))
        #the first 2tag in training data
        if training_data[0] and training_data[1] and training_data[0][1]!='.' and training_data[1][1]!='.':
            pi[training_data[0][1]][training_data[1][1]]+=1

        #loop through tuples
        for index in range(2,len(training_data)-2):
            #find the periods
            if training_data[index][1]=='.':
                total_sentences +=1
                #if order = 3, add one to the count of 2 sequential tag that comes after "."
                pi[training_data[index+1][1]][training_data[index+2][1]]+=1
        #normalize so that total probability is 1
        for key in pi:
            for key2 in pi[key]:
                 pi[key][key2]=pi[key][key2]/total_sentences
    return pi

training_data,unique_words,unique_tags = read_pos_file('training.txt')
#print(training_data)
#print(compute_counts(training_data,3))

def compute_emission_probabilities(unique_words: list, unique_tags: list, W: dict, C: dict) -> dict:
    '''
    input:
    - unique_words, set returned by read_pos_file
    - unique_tags, set returned by read_pos_file
    -W, dictionary C ( t i , w i ) computed by compute_counts
    -C,dictionary C ( t i ) computed by compute_counts 
    
    output:
    - the emission matrix as a dictionary whose keys are the tags.
    '''
    emission = defaultdict(lambda: defaultdict(int))
    for tag in unique_tags:
        for word in unique_words:
            p = W[tag][word]/C[tag]
            emission[tag][word]=p
    return emission


def compute_lambdas(unique_tags: list, num_tokens: int, C1: dict, C2: dict, C3: dict, order: int) -> list:
    '''
    implements Algorithm Compute lambda

    input:
    - unique_tags, set returned by read_pos_file
    - num_tokens, total number of tokens in training corpus (found by compute_counts)
    - order, the order of the HMM.
    - C1, C2, and C3 are the dictionaries with the counts  
    C ( t i ) ,  C ( t i − 1 , t i ) , and  C ( t i − 2 , t i − 1 , t i ) 

    output:
    - a list that contains  λ 0 ,  λ 1 , and  λ 2 , respectively
    '''
    unique_tags = list(unique_tags)
    lambdas = [0,0,0]
    if order == 3:
        for t_iminus2 in unique_tags:
            for t_iminus1 in unique_tags:
                for t_i in unique_tags:
                    alpha_0,alpha_1,alpha_2=0,0,0
                    #print('C3[t_iminus2][t_iminus1][t_i] ',C3[t_iminus2][t_iminus1][t_i])
                    if C3[t_iminus2][t_iminus1][t_i]>0:
                        if num_tokens>0:
                            alpha_0 = (C1[t_i]-1)/num_tokens
                        if (C1[t_iminus1]-1)>0 :
                            alpha_1 = (C2[t_iminus1][t_i]-1)/(C1[t_iminus1]-1)
                        if (C2[t_iminus2][t_iminus1]-1)>0:
                            alpha_2 = (C3[t_iminus2][t_iminus1][t_i]-1)/(C2[t_iminus2][t_iminus1]-1)
                        i = 0
                        if alpha_2 > alpha_1 and alpha_2>alpha_0:
                            i = 2
                        elif alpha_1 > alpha_0 and alpha_1>alpha_2:
                            i = 1

                        lambdas[i] = lambdas[i] + C3[t_iminus2][t_iminus1][t_i]
    if order == 2:
            # for i in range(1,len(unique_tags)):
            #     t_iminus1 = unique_tags[i-1]
            #     t_i = unique_tags[i]
            for t_iminus1 in unique_tags:
                for t_i in unique_tags:
                    alpha_0,alpha_1=0,0

                    if C2[t_iminus1][t_i]>0:
                        if num_tokens>0:
                            alpha_0 = (C1[t_i]-1)/num_tokens
                        if (C1[t_iminus1]-1)>0 :
                            alpha_1 = (C2[t_iminus1][t_i]-1)/(C1[t_iminus1]-1)
                        if alpha_0 >= alpha_1:
                            i = 0
                        else:
                            i=1

                        lambdas[i] = lambdas[i] + C2[t_iminus1][t_i]
    
    sums = sum(lambdas)

    lambdas = [each/sums for each in lambdas]
    
    return lambdas

def build_transition_matrix(lambdas,unique_tags, num_tokens, C1, C2, C3, order):
    if order == 2:
        transition_matrix = defaultdict(lambda: defaultdict(int))
        for t_i in unique_tags:
            for t_iminus1 in unique_tags:
                if C1[t_iminus1] > 0:
                    transition_matrix[t_iminus1][t_i] = lambdas[1]*C2[t_iminus1][t_i]/C1[t_iminus1]+lambdas[0]*C1[t_i]/num_tokens

    if order == 3:
        transition_matrix = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
        #print('...building transition_matrix with lambdas ',lambdas)
        for t_i in unique_tags:
            for t_iminus1 in unique_tags:
                for t_iminus2 in unique_tags:
                    if C2[t_iminus2][t_iminus1]>0:
                        val1 = lambdas[2]*float(C3[t_iminus2][t_iminus1][t_i])/C2[t_iminus2][t_iminus1]
                    else:
                        val1 = 0
                    if C1[t_iminus1]>0:
                        val2 =float(lambdas[1]*C2[t_iminus1][t_i])/C1[t_iminus1]
                    else:
                        val2 = 0
                    transition_matrix[t_iminus2][t_iminus1][t_i] = val1 + val2+lambdas[0]*float(C1[t_i])/num_tokens
    
    return transition_matrix
def build_hmm(training_data: list, unique_tags: list, unique_words: list, order: int, use_smoothing: bool):
    '''
	input 
	- training_data, a list of (word, POS-tag) pairs returned by the function read_pos_file
    - use_smoothing, a Boolean parameter. 
    
    Output
    - an (fully trained) HMM. 
    
    If use_smoothing is True, the function uses the  λ s as computed by 
    compute_lambdas; otherwise, it uses  λ 0 = λ 2 = 0  and  λ 1 = 1  
    in the case of a bigram mode, 
    and  λ 0 = λ 1 = 0  and  λ 2 = 1  in the case of a trigram model.
    '''
    
    if order == 2:
        #print('compute_counts...')
        num_tokens,c_ti_wi,C1,C2 = compute_counts(training_data, order)
        C3=defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
        if use_smoothing:
            #print('compute_lambdas...')
            lambdas = compute_lambdas(unique_tags, num_tokens, C1, C2, C3, order)
        else:
            lambdas = [0,1,0]
        #print('compute_initial_distribution')
        initial_distribution = compute_initial_distribution(training_data, order)
        #print('compute_emission_probabilities')
        emission_matrix = compute_emission_probabilities(unique_words, unique_tags, c_ti_wi, C1) 
        #print('build_transition_matrix')
        transition_matrix = build_transition_matrix(lambdas,unique_tags, num_tokens, C1, C2, C3, order)
    if order == 3:
        #print('compute_counts...')
        num_tokens,c_ti_wi,C1,C2,C3 = compute_counts(training_data, order)
        if use_smoothing:
            print('compute_lambdas...')
            lambdas = compute_lambdas(unique_tags, num_tokens, C1, C2, C3, order)
        else:
            lambdas = [0,0,1]
        #print('compute_initial_distribution')
        initial_distribution = compute_initial_distribution(training_data, order)
        #print('compute_emission_probabilities')
        emission_matrix = compute_emission_probabilities(unique_words, unique_tags, c_ti_wi, C1) 
        #print('build_transition_matrix')
        transition_matrix = build_transition_matrix(lambdas,unique_tags, num_tokens, C1, C2, C3, order)
    
    hmm = HMM(order, initial_distribution, emission_matrix, transition_matrix)
    return hmm

#testing
# unique_words = ['hw7', 'is', 'difficult', '.']
# unique_tags = ['N', 'V', 'A', '.']
# training_data = [('hw7','N'), ('is','V'),('difficult','A'),('.','.')]
# hmm = build_hmm(training_data, unique_tags, unique_words,3 ,False)
#print('transition matrix is: ',hmm.transition_matrix)
#2 smoothing????
#{'N':  {'V': 0.25}), 'V':  {'A': 0.25}), 'A':  {'.': 0.25})})
#2 no smoothing
#{'N':  {'V': 1.0}), 'V': {'A': 1.0}), 'A':  {'.': 1.0})})
#order 3 no smoothing
# {'N': defaultdict(<function build_transition_matrix.<locals>.<lambda>.<locals>.<lambda> at 0x106a01870>, 
#     {'V': defaultdict(<class 'int'>, 
#         {'A': 0.0})}), '
# V': defaultdict(<function build_transition_matrix.<locals>.<lambda>.<locals>.<lambda> at 0x106a01900>, 
#     {'A': defaultdict(<class 'int'>, {
#         '.': 0.0})})})

#print('initial_distribution is: ',hmm.initial_distribution)
# {'N': 1.0}

#print('emission_matrix is: ',hmm.emission_matrix)
#with smoothing
#{'N': defaultdict(<class 'int'>, {'hw7': 1.0, 'is': 0.0, 'difficult': 0.0, '.': 0.0}), 'V': defaultdict(<class 'int'>, {'hw7': 0.0, 'is': 1.0, 'difficult': 0.0, '.': 0.0}), 'A': defaultdict(<class 'int'>, {'hw7': 0.0, 'is': 0.0, 'difficult': 1.0, '.': 0.0}), '.': defaultdict(<class 'int'>, {'hw7': 0.0, 'is': 0.0, 'difficult': 0.0, '.': 1.0})})


def trigram_viterbi(hmm, sentence: list) -> list:
    """
    !!!!!!!!!
    Run the Viterbi algorithm to tag a sentence assuming a bigram HMM model.
    Inputs:
      hmm --- the HMM to use to predict the POS of the words in the sentence.
      sentence ---  a list of words.
    Returns:
      A list of tuples where each tuple contains a word in the
      sentence and its predicted corresponding POS.
    """
    # Initialization
    # viterbi = defaultdict(lambda: defaultdict(int))
    # backpointer = defaultdict(lambda: defaultdict(int))
    viterbi = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
    backpointer = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
    unique_tags = set(hmm.initial_distribution.keys()).union(set(hmm.transition_matrix.keys()))
    for tag1 in unique_tags:
        for tag2 in unique_tags:
            if (hmm.initial_distribution[tag1][tag2] != 0) and (hmm.emission_matrix[tag1][sentence[0]] != 0) and (hmm.emission_matrix[tag2][sentence[1]] != 0):
                viterbi[tag1][tag2][1] = math.log(hmm.initial_distribution[tag1][tag2]) + math.log(hmm.emission_matrix[tag1][sentence[0]])+ math.log(hmm.emission_matrix[tag2][sentence[1]])
            else:
                viterbi[tag1][tag2][1] = -1 * float('inf')



    # Dynamic programming.
    for i in range(2, len(sentence)):
        backpointer["No_Path"]["No_Path"][i] = "No_Path"
        for l in unique_tags:
            for l_prime in unique_tags:
                max_value = -1 * float('inf')
                max_state = None
                #find max l’’ ∈S(v[l’’,l’,i-1] * Al’’,l’,l)
                for l_prime_prime in unique_tags:
                    val1= viterbi[l_prime_prime][l_prime][i-1]
                    val2 = -1 * float('inf')
                    if hmm.transition_matrix[l_prime_prime][l_prime][l] != 0:
                        val2 = math.log(hmm.transition_matrix[l_prime_prime][l_prime][l])
                    curr_value = val1 + val2
                    if curr_value > max_value:
                        max_value = curr_value
                        max_state = l_prime_prime
                #val3 is  El(Xi)
                val3 = -1 * float('inf')
                if hmm.emission_matrix[l][sentence[i]] != 0:
                    val3 = math.log(hmm.emission_matrix[l][sentence[i]])
                viterbi[l_prime][l][i] = max_value + val3
                if max_state == None:
                    backpointer[l_prime][l][i] = "No_Path"
                else:
                    backpointer[l_prime][l][i] = max_state
    # for ut in unique_tags:
    #         for ut_prime in unique_tags:
    #             string = ""
    #             for i in range(0, len(sentence)):
    #                 if (viterbi[ut][ut_prime][i] != float("-inf")):
    #                     string += str(int(viterbi[ut][ut_prime][i])) + "\t"
    #                 else:
    #                     string += str(viterbi[ut][ut_prime][i]) + "\t"

    # Termination
    max_value = -1 * float('inf')
    last_state, second_last_state = None, None
    final_time = len(sentence) - 1
    for l_prime_prime in unique_tags:
        for l_prime in unique_tags:
            if viterbi[l_prime_prime][l_prime][final_time] > max_value:
                max_value = viterbi[l_prime_prime][l_prime][final_time]
                second_last_state = l_prime_prime
                last_state = l_prime
    if last_state == None:
        last_state = "No_Path"
    if second_last_state == None:
        second_last_state = "No_Path"

    # Traceback
    tagged_sentence = []
    tagged_sentence.append((sentence[len(sentence)-1], last_state))
    tagged_sentence.append((sentence[len(sentence)-2], second_last_state))
    #for i ←L −3 down to 0 do
    #Zi ←bp[Zi+1,Zi+2, i + 2];
    for i in range(len(sentence)-3, -1, -1):
        next_tag = tagged_sentence[-1][1]
        next_next_tag = tagged_sentence[-2][1]
        curr_tag = backpointer[next_tag][next_next_tag][i+2]
        tagged_sentence.append((sentence[i], curr_tag))
    tagged_sentence.reverse()
    return tagged_sentence

#ans = bigram_viterbi(hmm, unique_words)
#print(ans)