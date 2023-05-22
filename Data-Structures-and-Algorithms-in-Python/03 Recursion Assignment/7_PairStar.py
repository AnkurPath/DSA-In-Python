# Pair Star
# Send Feedback
# Given a string S, compute recursively a new string where identical chars that are adjacent in the original string are separated from each other by a "*".
# Input format :
# String S
# Output format :
# Modified string
# Constraints :
# 0 <= |S| <= 1000
# where |S| represents length of string S.
# Sample Input 1 :
# hello
# Sample Output 1:
# hel*lo
# Sample Input 2 :
# aaaa
# Sample Output 2 :


from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.


def pairStar(st, Output, i=0):
    Output = Output + Input[i]

    if (i == len(st) - 1):
        print(Output)
        return;

    if (st[i] == st[i + 1]):
        Output = Output + '*'

    pairStar(st, Output, i + 1)

if __name__ == "__main__":
    Input = input()
    Output = ""
    pairStar(Input, Output)


