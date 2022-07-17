"""
Searching Exercise 5: Search value in mxn Matrix
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

For Example, consider the following matrix:
[ [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]]

  [[1,  4,  7, 11, 15,20],
  [2,   5,  8, 12, 19,21],
  [3,   6,  9, 16, 22,25],
  [10, 13, 14, 17, 24,31],
  [18, 21, 23, 26, 30,40]

Target  = 5, Return value = true
Target = 20. Return value = false
"""


def searchMXN(matrix,target):
    w = len(matrix[0])
    for row in matrix:
        if row[0]<=target<=row[-1]:
            l,r = 0,w-1
            while l<=r:
                mid = (l+r)//2
                if row[mid] == target:
                    return True
                elif row[mid] > target:
                    r=mid-1
                else:
                    l = mid+1

    return False
                

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 20
target = 5
print(searchMXN(matrix,target))