"""Given an array of size n and an integer k, return the count of distinct numbers in all windows of size k."""


def distinct(arr,k):
    result = []
    if len(arr)<k:
        return result
    for i in range(len(arr)-k+1):
        window_length =len(set(arr[i:i+k]))
        result.append(window_length)
    return result



arr= [1, 2, 1, 3, 4, 2, 3]
k = 4

arr= [1, 2, 4, 4]
k = 2

print(distinct(arr,k))
