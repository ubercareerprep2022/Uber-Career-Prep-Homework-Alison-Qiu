"""
Sorting Exercise 5: Peaks and Valleys
In an array of integers, a "peak" is an element that is greater than or equal to the adjacent integers and a "valley" is an element that 
is less than or equal to the adjacent integers. For example, in the array [5, 8, 6, 2, 3, 4, 6], [8, 6] are peaks and [5, 2] are valleys. 
Given an array of integers, sort the array into an alternating sequence of peaks and valleys.

Example
Input: [5, 3, 1, 2, 3]
Output: [5, 1, 3, 2, 3]

"""
def quickSort( arr,start,end):
    l,r = start,end
    if end-start<=1:
        if arr[start]>arr[end]:
            arr[start],arr[end] = arr[end],arr[start]
    else:
        l,r = start,end
        pivot = arr[(l+r)//2]
        while l<=r:
            while l<=r and arr[l]<pivot:
                l+=1
            while l<=r and arr[r]>pivot:
                r-=1               
            if r>=l:
                arr[l],arr[r]=arr[r],arr[l]
                l+=1
                r-=1

        quickSort(arr,start,r)
        quickSort(arr,l,end)


def PeaksAndValleys(arr):
    if len(arr)<=1:
        return arr
    quickSort(arr,0,len(arr)-1)
    #print(arr)
    # i = 0
    # while i<len(arr)-1:
    #     if arr[i] != arr[i+1]:
    #         arr[i],arr[i+1] = arr[i+1],arr[i]
    #         i+=2
    #     else:
    #         i+=1

    for i in range(0,len(arr)-1,2):
        arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr



def PeaksAndValleys2(arr):
    for i in range(1,len(arr)-1,2):
        if arr[i]>arr[i-1]:
            arr[i], arr[i-1] = arr[i-1], arr[i]
        if arr[i]>arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

test_cases = [
    {
        'arr': [5,6, 3, 4, 1, 2, 3],
        'res': ([2, 1, 3, 4, 3, 6, 5])

    },
    {
        'arr': [],
        'res': ([])

    },
    {
        'arr': [1],
        'res': ([1])

    },
    {
        'arr': [2,2,1],
        'res': ([2,1,2])

    },
    {
        'arr': [5, 3, 1, 2, 3],
        'res': ([5, 1, 3, 2, 3],[2, 1, 3, 3, 5])

    }
]

for case in test_cases:
    print(PeaksAndValleys2(case['arr']))
