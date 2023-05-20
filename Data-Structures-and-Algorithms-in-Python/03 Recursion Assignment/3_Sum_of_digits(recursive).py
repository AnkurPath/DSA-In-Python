# Sum of digits (recursive)
# Send Feedback
# Write a recursive function that returns the sum of the digits of a given integer.
# Input format :
# Integer N
# Output format :
# Sum of digits of N
# Constraints :
# 0 <= N <= 10^9
# Sample Input 1 :
# 12345
# Sample Output 1 :
# 15
# Sample Input 2 :
# 9
# Sample Output 2 :
# 9



from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.


def sumOfDigit(n):
    inputForNext=n//10
    addValue=n%10
    if inputForNext==0:
        return addValue
    return addValue + sumOfDigit(inputForNext)

n=int(input())
print(sumOfDigit(n))






