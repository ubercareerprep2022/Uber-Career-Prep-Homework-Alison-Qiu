import math

def mergeSort(arr):
    if len(arr)>1:
        mid =  len(arr)//2
        l = arr[:mid]
        r = arr[mid:]
        mergeSort(l)
        mergeSort(r)

        l_index = r_index = arr_index = 0
        while l_index<len(l) and r_index< len(r):
            if l[l_index]>r[r_index]:
                arr[arr_index] = r[r_index]
                r_index += 1
            else:
                arr[arr_index] = l[l_index]
                l_index += 1
            arr_index+=1

        while l_index<len(l):
            arr[arr_index] = l[l_index]
            l_index += 1
            arr_index+=1

        while r_index<len(r):
            arr[arr_index] = r[r_index]
            r_index += 1
            arr_index+=1

    return arr

def binarySearch(arr,num):
    l = 0
    r = len(arr)-1
    while l<=r:
 
        mid = (l+r)//2
        if arr[mid] < num:
                l = mid + 1
        elif arr[mid] > num:
                r = mid - 1
        else:
                return True
    return False
 

def isStringPermutation(s1: str, s2: str) -> bool:
    ''' 
    takes two Strings as parameters and returns a Boolean 
    denoting whether the first string is a permutation of the second string
    '''
    return mergeSort(list(s1)) == mergeSort(list(s2))


#print(isStringPermutation('asdf','fsad'))
#true
# isStringPermutation(s1: “asdf”, s2: “fsa”) == false
# isStringPermutation(s1: “asdf”, s2: “fsax”) == false



def pairsThatEqualSum(inputArray: list, targetSum: int) -> list:
    '''
    input:
    - an array of integers 
    - a target integer
    
    output: 
    - an array of pairs (i.e., an array of tuples) where each 
    pair contains two numbers from the input array 
    and the sum of each pair equals the target integer. 
    (Order of the output does not matter).
    '''
    ans = []
    #sort the inputArray 
    sorted_input = mergeSort(inputArray)

    #for each element of the sorted array minus  
    # that element, binary search diff = targetSum-element
    # if found add (element,diff) to ans
    for i in range(int(math.ceil(len(sorted_input)/2))):
        diff = targetSum-sorted_input[i]
        if binarySearch(sorted_input[:i-1]+sorted_input[i:],diff):
            ans.append((sorted_input[i],diff))
    
    return list(ans)


#print(pairsThatEqualSum([1, 2, 3, 4, 5],5))
#print(pairsThatEqualSum([1, 2, 3, 4, 5],1))
print(pairsThatEqualSum([1, 2, 3, 4, 5],7))