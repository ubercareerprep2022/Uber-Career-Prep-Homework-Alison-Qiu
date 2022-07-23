"""
Implement pow(x, n), which calculates x raised to the power n. 
Example 3.1
Input: x = 2.0, n = 10
Output: 1024.0
Example 3.2
Input: x = 2.0, n = -2
Output: 0.25
Explanation: 2-2 ⇒ 1/(2*2) ⇒ 1/4 ⇒ 0.25
"""

#2^10 = 2^5 *2^5
#2^-2 = 2^-1 

def pow(x, n):
    if n == 0: 
        return 1
    elif n==1:
        return x
    elif n==-1:
        return 1/x
    else:
        return pow(x, n//2)*pow(x, n-n//2)

print(pow(2,10))
print(pow(2,-2))