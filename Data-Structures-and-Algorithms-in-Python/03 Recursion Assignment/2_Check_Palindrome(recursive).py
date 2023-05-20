# Check Palindrome (recursive)
# Send Feedback
# Check whether a given String S is a palindrome using recursion. Return true or false.
# Input Format :
# String S
# Output Format :
# 'true' or 'false'
# Constraints :
# 0 <= |S| <= 1000
# where |S| represents length of string S.
# Sample Input 1 :
# racecar
# Sample Output 1:
# true
# Sample Input 2 :
# ninja
# Sample Output 2:
# false

from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.

def isPalRec(st, s, e) :
    if (s == e):
        return True

    if (st[s] != st[e]) :
        return False
 
    if (s < e + 1) :
        return isPalRec(st, s + 1, e - 1);
 
    return True
 
def isPalindrome(st) :
    n = len(st)
     
    if (n == 0) :
        return True
     
    return isPalRec(st, 0, n - 1);
 
st=input()
if (isPalindrome(st)) :
    print('true')
else :
    print('false')
