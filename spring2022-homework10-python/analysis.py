# Firstname Lastname
# NetID
# COMP 182 Spring 2021 - Homework 8, Problem 2

# You can import any standard library, as well as Numpy and Matplotlib.
# You can use helper functions from provided.py, and autograder.py,
# but they have to be copied over here.

# Your code here...
from numpy import percentile
from autograder import *
import matplotlib.pyplot as plt
import pylab
import math
import copy

def update_hmm(hmm,unique_words_testing,training_words):
    '''
    update the emission matrix
    training_words: list of words from training data
    '''

    #For every word w in the test data that is not in the training data
    for word in unique_words_testing:
        if word not in training_words:
            #assign a very small emission probability of that word from each state 
            for state in hmm.emission_matrix:
                hmm.emission_matrix[state][word] = 0.00001
                # #adjust the non-zero emission probabilities of other words from all states by adding the same  to them. 
                for old_word in hmm.emission_matrix[state]:
                    hmm.emission_matrix[state][old_word] += 0.00001               
        # else:
        #     for state in hmm.emission_matrix:
        #         hmm.emission_matrix[state][word] += 0.00001
    #normalize
    for state in hmm.emission_matrix:
        total = 0
        for word in hmm.emission_matrix[state]:
            total+=hmm.emission_matrix[state][word]
        for word in hmm.emission_matrix[state]:
            hmm.emission_matrix[state][word] = hmm.emission_matrix[state][word]/total
        


    # for state in hmm.emission_matrix:
    #     total = 0
    #     for word in unique_words_testing:
    #         hmm.emission_matrix[state][word] += 0.00001
    #         total += hmm.emission_matrix[state][word]
    #     for any_word in state:
    #         if any_word not in unique_words_testing:
    #             hmm.emission_matrix[state][any_word] += 0.00001
    #             total += hmm.emission_matrix[state][any_word]
    #     #normalize the emission values for each state so that they add up to 1
    #     for word in state:
    #         hmm.emission_matrix[state][word] = hmm.emission_matrix[state][word]/total

def compute_accuracy(testing_result,ground_truth):
    '''
    computes the percent of correct result 
    '''   
    total = 0
    correct = 0   
    for ind in range(len(testing_result)):
        total+=1
        if testing_result[ind]==ground_truth[ind]:
            correct += 1
    return correct/total

    # for tuple in testing_result:
    #     total+=1
    #     if tuple in ground_truth:
    #         correct += 1
    # return correct/total

def get_untagged_words(filename):
    f = open(str(filename), "r")
    #word = f.read().split(" ")
    words = []
    for line in f:
        list_words = line.split()
        for word in list_words:
            words.append(word)
    f.close()
    return words

def _dict2lists(data):
    """
    Convert a dictionary into a list of keys and values, sorted by
    key.  

    Arguments:
    data -- dictionary

    Returns:
    A tuple of two lists: the first is the keys, the second is the values
    """
    xvals = list(data.keys())
    xvals.sort()
    yvals = []
    for x in xvals:
        yvals.append(data[x])
    return xvals, yvals

def _plot_dict_line(d, label=None):
    """
    Plot data in the dictionary d on the current plot as a line.

    Arguments:
    d     -- dictionary
    label -- optional legend label

    Returns:
    None
    """
    xvals, yvals = _dict2lists(d)
    if label:
        pylab.plot(xvals, yvals, label=label)
    else:
        pylab.plot(xvals, yvals)

def plot_lines(data, title, xlabel, ylabel, labels=None, filename=None):
    """
    Plot a line graph with the provided data.

    Arguments: 
    data     -- a list of dictionaries, each of which will be plotted 
                as a line with the keys on the x axis and the values on
                the y axis.
    title    -- title label for the plot
    xlabel   -- x axis label for the plot
    ylabel   -- y axis label for the plot
    labels   -- optional list of strings that will be used for a legend
                this list must correspond to the data list
    filename -- optional name of file to which plot will be
                saved (in png format)

    Returns:
    None
    """
    ### Check that the data is a list
    if not isinstance(data, list):
        msg = "data must be a list, not {0}".format(type(data).__name__)
        raise TypeError(msg)

    ### Create a new figure
    fig = pylab.figure()

    ### Plot the data
    if labels:
        mylabels = labels[:]
        for _ in range(len(data)-len(labels)):
            mylabels.append("")
        for d, l in zip(data, mylabels):
            _plot_dict_line(d, l)
        # Add legend
        pylab.legend(loc='best')
        gca = pylab.gca()
        legend = gca.get_legend()
        pylab.setp(legend.get_texts(), fontsize='medium')
    else:
        for d in data:
            _plot_dict_line(d)

    ### Set the lower y limit to 0 or the lowest number in the values
    mins = [min(l.values()) for l in data]
    ymin = min(0, min(mins))
    pylab.ylim(ymin=ymin)

    ### Label the plot
    pylab.title(title)
    pylab.xlabel(xlabel)
    pylab.ylabel(ylabel)

    ### Draw grid lines
    pylab.grid(True)

    ### Show the plot
    fig.show()

    ### Save to file
    if filename:
        pylab.savefig(filename)

def show():
    """
    Do not use this function unless you have trouble with figures.

    It may be necessary to call this function after drawing/plotting
    all figures.  If so, it should only be called once at the end.

    Arguments:
    None

    Returns:
    None
    """
    plt.show()

print('getting training_data ')
training_data,training_words = read_pos_file('training.txt')[0],read_pos_file('training.txt')[1]
print('getting testdata_tagged ')
testdata_tagged = read_pos_file('testdata_tagged.txt')[0]
#testdata_words = [tuple[0] for tuple in testdata_tagged]
print('getting testdata_words ')
testdata_words = get_untagged_words('testdata_untagged.txt')

#compute indices to slice at for different percentages
percent_list = []
one_percent = int(len(training_data)*0.01)
five_percent = int(len(training_data)*0.05)
ten_percent = int(len(training_data)*0.1)
twentyfive_percent = int(len(training_data)*0.25)
fifty_percent = int(len(training_data)*0.5)
seventyfive_percent = int(len(training_data)*0.75)
percent_list.append((0.01,one_percent))
percent_list.append((0.05,five_percent))
percent_list.append((0.1,ten_percent))
percent_list.append((0.25,twentyfive_percent))
percent_list.append((0.5,fifty_percent))
percent_list.append((0.75,seventyfive_percent))
percent_list.append((1,int(len(training_data))))


#experiment 1: bigram no smoothing
bigram_nosmoothing = {}
for percent in percent_list:
    training = training_data[:percent[1]]
    words, tags = set(),set()
    for data in training:
        words.add(data[0])
        tags.add(data[1])
    # words = [data[0] for data in training]
    # tags = [data[1] for data in training]
    #print('building hmm...')
    bigram_false = build_hmm(training, tags, words,2 ,False)
    update_hmm(bigram_false,testdata_words,words)
    bigram_false_result = bigram_viterbi(bigram_false, testdata_words)
    bigram_false_accuracy = compute_accuracy(bigram_false_result,testdata_tagged)
    #print('prediction: ',bigram_false_result)
    print('bigram_false_accuracy for',percent[0], 'is ',bigram_false_accuracy)
    bigram_nosmoothing[percent[0]]=bigram_false_accuracy

# #experiment 2: trigram no smoothing
trigram_nosmoothing = {}
for percent in percent_list:
    training = training_data[:percent[1]]
    words, tags = set(),set()
    for data in training:
        words.add(data[0])
        tags.add(data[1])
    #print('building hmm...')
    trigram_false = build_hmm(training, tags, words,3 ,False)
    update_hmm(trigram_false,testdata_words,words)
    trigram_false_result = trigram_viterbi(trigram_false, testdata_words)
    trigram_false_accuracy = compute_accuracy(trigram_false_result,testdata_tagged)
    #print('prediction: ',bigram_false_result)
    print('trigram_false_accuracy for',percent[0], 'is ',trigram_false_accuracy)
    trigram_nosmoothing[percent[0]]=trigram_nosmoothing

# #experiment 3: bigram with smoothing
bigram_smoothing ={}
for percent in percent_list:
    training = training_data[:percent[1]]
    words, tags = set(),set()
    for data in training:
        words.add(data[0])
        tags.add(data[1])
    # words = [data[0] for data in training]
    # tags = [data[1] for data in training]
    #print('building hmm...')
    bigram_true = build_hmm(training, tags, words,2 ,True)
    update_hmm(bigram_true,testdata_words,words)
    bigram_true_result = bigram_viterbi(bigram_true, testdata_words)
    bigram_true_accuracy = compute_accuracy(bigram_true_result,testdata_tagged)
    #print('prediction: ',bigram_false_result)
    print('bigram_true_accuracy for',percent[0], 'is ',bigram_true_accuracy)
    bigram_smoothing[percent[0]]=bigram_true_accuracy

# #experiment 4: trigram with smoothing
trigram_smoothing = {}
for percent in percent_list:
    training = training_data[:percent[1]]
    words, tags = set(),set()
    for data in training:
        words.add(data[0])
        tags.add(data[1])
    #print('building hmm...')
    trigram_true = build_hmm(training, tags, words,3 ,True)
    update_hmm(trigram_true,testdata_words,words)
    trigram_true_result = trigram_viterbi(trigram_true, testdata_words)
    trigram_true_accuracy = compute_accuracy(trigram_true_result,testdata_tagged)
    #print('prediction: ',bigram_false_result)
    print('trigram_true_accuracy for',percent[0], 'is ',trigram_true_accuracy)
    trigram_smoothing[percent[0]]=trigram_true_accuracy

# bigram_nosmoothing={0.01:0.7802874743326489,0.05:0.8829568788501027,0.10:0.8973305954825462,0.25: 0.9281314168377823,0.50: 0.9322381930184805,0.75:0.9404517453798767,1.00:0.9435318275154004}
# trigram_nosmoothing={0.01:0.7628336755646817,0.05:0.8767967145790554,0.10:0.9045174537987679,0.25: 0.9332648870636551,0.50: 0.9332648870636551,0.75:0.9383983572895277,1.00:0.9435318275154004}
# bigram_smoothing={0.01:0.7792607802874744,0.05:0.8870636550308009,0.10:0.9065708418891171,0.25: 0.9332648870636551,0.50: 0.9383983572895277,0.75:0.9476386036960985,1.00:0.9486652977412731}
# trigram_smoothing={0.01:0.7854209445585215,0.05:0.8901437371663244,0.10:0.9168377823408624,0.25: 0.9404517453798767,0.50: 0.9435318275154004,0.75:0.9476386036960985,1.00:0.9548254620123203}

plot_lines(
    [bigram_nosmoothing,trigram_nosmoothing,bigram_smoothing,trigram_smoothing],
'largest connected component vs number of nodes removed under random and targeted attacks', 
'percentages of training data used', 
'largest connected component size (in number of nodes)', 
labels=['bigram_nosmoothing','trigram_nosmoothing','bigram_smoothing','trigram_smoothing'],
filename=None)
show()