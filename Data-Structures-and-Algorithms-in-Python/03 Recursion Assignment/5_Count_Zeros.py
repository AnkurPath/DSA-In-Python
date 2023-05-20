# Count Zeros
# Send Feedback
# Given an integer N, count and return the number of zeros that are present in the given integer using recursion.
# Input Format :
# Integer N
# Output Format :
# Number of zeros in N
# Constraints :
# 0 <= N <= 10^9
# Sample Input 1 :
# 0
# Sample Output 1 :
# 1
# Sample Input 2 :
# 00010204
# Sample Output 2 :
# 2
# Explanation for Sample Output 2 :
# Even though "00010204" has 5 zeros, the output would still be 2 because when you convert it to an integer, it becomes 10204.
# Sample Input 3 :
# 708000
# Sample Output 3 :
# 4

from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.



count=0
def count_digit(num):
    global count
    if num==0:
        return 1
    if (num >0):
        if(num%10==0):
            count +=1
        count_digit(num // 10)
    return count
n=int(input())
print(count_digit(n))

