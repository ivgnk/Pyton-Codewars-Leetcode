"""
Done 08.05.2024. Topics: Math
1716. Calculate Money in Leetcode Bank
https://leetcode.com/problems/calculate-money-in-leetcode-bank/description/

Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.
He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday,
he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.
Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.

Example 1:
Input: n = 4
Output: 10
Explanation: After the 4th day, the total is 1 + 2 + 3 + 4 = 10.

Example 2:
Input: n = 10
Output: 37
Explanation: After the 10th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) = 37. Notice that on the 2nd Monday, Hercy only puts in $2.

Example 3:
Input: n = 20
Output: 96
Explanation: After the 20th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96.
"""

# Runtime 13 ms Beats 71.96% of users with Python
# Memory 11.57 MB Beats 69.84% of users with Python

def sum_ar_p(f,n):
    return (2*f+(n-1))*n//2

def totalMoney(n):
    """
    :type n: int
    :rtype: int
    """
    weeks=n//7; w1=weeks+1
    ldays=n%7
    res = [sum_ar_p(i,7) for i in range(1,w1)]
    ldw=sum_ar_p(w1,ldays)
    return sum(dat for dat in res)+ldw

# print(totalMoney(4))
# print(totalMoney(10))
print(totalMoney(20))