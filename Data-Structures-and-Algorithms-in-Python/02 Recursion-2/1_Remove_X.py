# Remove X
# Send Feedback
# Given a string, compute recursively a new string where all 'x' chars have been removed.
# Input format :
# String S
# Output format :
# Modified String
# Constraints :
# 1 <= |S| <= 10^3
# where |S| represents the length of string S. 
# Sample Input 1 :
# xaxb
# Sample Output 1:
# ab
# Sample Input 2 :
# abc
# Sample Output 2:
# abc
# Sample Input 3 :
# xx
# Sample Output 3:

# Problem: Remove x from string
def removeX(string):
    if len(string)==0:
        return string
    smallerStringOutput=removeX(string[1:])
    if string[0]=="x":
        return ""+smallerStringOutput
    else:
        return string[0]+smallerStringOutput


# Main
string = input()
print(removeX(string))
