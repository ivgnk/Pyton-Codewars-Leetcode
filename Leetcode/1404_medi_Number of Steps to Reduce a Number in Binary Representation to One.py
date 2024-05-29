"""
Done 29.05.2024. Topics: String
1404. Number of Steps to Reduce a Number in Binary Representation to One
https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/description/

Given the binary representation of an integer as a string s, return the number of steps to reduce it to 1 under the following rules:
If the current number is even, you have to divide it by 2.
If the current number is odd, you have to add 1 to it.
It is guaranteed that you can always reach one for all test cases.

Example 1:
Input: s = "1101"
Output: 6
Explanation: "1101" corressponds to number 13 in their decimal representation.
Step 1) 13 is odd, add 1 and obtain 14.
Step 2) 14 is even, divide by 2 and obtain 7.
Step 3) 7 is odd, add 1 and obtain 8.
Step 4) 8 is even, divide by 2 and obtain 4.
Step 5) 4 is even, divide by 2 and obtain 2.
Step 6) 2 is even, divide by 2 and obtain 1.

Example 2:
Input: s = "10"
Output: 1
Explanation: "10" corressponds to number 2 in their decimal representation.
Step 1) 2 is even, divide by 2 and obtain 1.

Example 3:
Input: s = "1"
Output: 0

Hint 1
Read the string from right to left, if the string ends in '0' then the number is even otherwise it is odd.
Hint 2
Simulate the steps described in the binary string.
"""

# Runtime 20 ms Beats 36.36% of users with Python
# Memory 11.63 MB Beats 64.94% of users with Python
# Runtime 11 ms Beats 89.61% of users with Python
# Memory 11.40 MB Beats 100.00% of users with Python

def numSteps(s):
    """
    :type s: str
    :rtype: int
    """
    s1='0b'+s
    i=int(s1,2)
    n=0
    while i !=1:
        if i%2==0:
            i= i//2
        else:
            i=i+1
        n=n+1
    return n
print(numSteps('1101'))
# s=bin(13)
# print(s,int(s,2))