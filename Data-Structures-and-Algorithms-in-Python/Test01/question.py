Recurrence Relation for Tower of Hanoi Problem
Send Feedback
Q. No.1- The recurrence relation capturing the optimal execution time of the Towers of Hanoi problem with n discs is :

T(n) = 2T(n − 1) + 1


Complexity of different operations in a sorted array.
Send Feedback
Q. No.2- Which of the following operations is not O(1) for an array of sorted data. You may assume that array elements are distinct.

Delete an element

Complexity of a Recurrence Relation
Send Feedback
Q. No.3- Which one of the following correctly determines the solution of the recurrence relation with T(1) = 1?
T(n) = 2T(n/2) + Logn

O(N)
https://files.codingninjas.in/step1-10997.jpg
  
Q. No.4-
# Does s contain t ?
# Send Feedback
# Given two string s and t, write a function to check if s contains all characters of t (in the same order as they are in string t).
# Return true or false.
# Do it recursively.
# E.g. : s = “abchjsgsuohhdhyrikkknddg” contains all characters of t=”coding” in the same order. So function will return true.
# Input Format :
# Line 1 : String s
# Line 2 : String t
# Output Format :
# true or false
# Sample Input 1 :
# abchjsgsuohhdhyrikkknddg
# coding
# Sample Output 1 :
# true
# Sample Input 2 :
# abcde
# aeb
# Sample Output 2 :
# false

def contains(s,t):
    #Implement This Function Here
    if len(t) == 0:
        return True
    if len(s) == 0:
        return False
    
    # Recursive case
    if s[0] == t[0]:
        return contains(s[1:], t[1:])
    else:
        return contains(s[1:], t)

s = input()
t = input()

ans = contains(s,t)
if ans is True:
    print('true')
else:
    print('false')
    
Q. No.5-
# Maximum Profit on App
# Send Feedback
# You have made a smartphone app and want to set its subscription price such that the profit earned is maximised. There are certain users who will subscribe to your app only if their budget is greater than or equal to your price.
# You will be provided with a list of size N having budgets of subscribers and you need to return the maximum profit that you can earn.
# Lets say you decide that price of your app is Rs. x and there are N number of subscribers. So maximum profit you can earn is :
#  m * x
# where m is total number of subscribers whose budget is greater than or equal to x.
# Input format :
# Line 1 : N (No. of subscribers)
# Line 2 : Budget of subscribers (separated by space)
# Output Format :
#  Maximum profit
# Constraints :
# 1 <= N <= 10^6
# 1 <=budget[i]<=9999
# Sample Input 1 :
# 4
# 30 20 53 14
# Sample Output 1 :
# 60
# Sample Output 1 Explanation :
# Price of your app should be Rs. 20 or Rs. 30. For both prices, you can get the profit Rs. 60.
# Sample Input 2 :
# 5
# 34 78 90 15 67
# Sample Output 2 :
# 201
# Sample Output 2 Explanation :
# Price of your app should be Rs. 67. You can get the profit Rs. 201 (i.e. 3 * 67).



def maximumProfit(N):
		budgets.sort()
		max_profit=0
		for i in range(N):
			price = budgets[i]
			subscribers = N - i
			profit = price * subscribers

			if profit > max_profit:
				max_profit = profit

		return max_profit

n = int(input())
arr = [int(ele) for ele in input().split()]
ans = maximumProfit(arr,n)
print(ans)

Q. No.6-
# Split Array
# Send Feedback
# Given an integer array A of size N, check if the input array can be splitted in two parts such that -
# - Sum of both parts is equal
# - All elements in the input, which are divisible by 5 should be in same group.
# - All elements in the input, which are divisible by 3 (but not divisible by 5) should be in other group.
# - Elements which are neither divisible by 5 nor by 3, can be put in any group.
# Groups can be made with any set of elements, i.e. elements need not to be continuous. And you need to consider each and every element of input array in some group.
# Return true, if array can be split according to the above rules, else return false.
# Note : You will get marks only if all the test cases are passed.
# Input Format :
# Line 1 : Integer N (size of array)
# Line 2 : Array A elements (separated by space)
# Output Format :
# true or false
# Constraints :
# 1 <= N <= 50
# Sample Input 1 :
# 2
# 1 2
# Sample Output 1 :
# false
# Sample Input 2 :
# 3
# 1 4 3
# Sample Output 2 :
# true
    
def split(arr):
    totalSum = sum(arr)
    if totalSum % 2 != 0:
        return False

    targetSum = totalSum // 2
    memo = [[None] * (targetSum + 1) for _ in range(len(arr))]
    return canSplit(arr, 0, 0, targetSum, memo)

def canSplit(arr, currentIndex, currentSum, targetSum, memo):
    if currentIndex == len(arr) or currentSum > targetSum:
        return False

    if currentSum == targetSum:
        return True

    if memo[currentIndex][currentSum] is not None:
        return memo[currentIndex][currentSum]

    element = arr[currentIndex]
    divisibleBy3 = element % 3 == 0 and element % 5 != 0

    included = canSplit(arr, currentIndex + 1, currentSum + element, targetSum, memo)
    excluded = canSplit(arr, currentIndex + 1, currentSum, targetSum, memo)

    memo[currentIndex][currentSum] = included or excluded or divisibleBy3
    return memo[currentIndex][currentSum]


    
n = input()
arr = [int(ele) for ele in input().split()]
ans = split(arr)
if ans is True:
    print('true')
else:
    print('false')
  
  
  

