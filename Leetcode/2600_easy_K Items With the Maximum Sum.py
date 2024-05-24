"""
Done 24.05.2025. Topics: Math, Greedy

2600. K Items With the Maximum Sum
https://leetcode.com/problems/k-items-with-the-maximum-sum/description/

There is a bag that consists of items, each item has a number 1, 0, or -1 written on it.
You are given four non-negative integers numOnes, numZeros, numNegOnes, and k.
The bag initially contains:

numOnes items with 1s written on them.
numZeroes items with 0s written on them.
numNegOnes items with -1s written on them.
We want to pick exactly k items among the available items. Return the maximum possible sum of numbers written on the items.



Example 1:

Input: numOnes = 3, numZeros = 2, numNegOnes = 0, k = 2
Output: 2
Explanation: We have a bag of items with numbers written on them {1, 1, 1, 0, 0}.
We take 2 items with 1 written on them and get a sum in a total of 2.
It can be proven that 2 is the maximum possible sum.

Example 2:

Input: numOnes = 3, numZeros = 2, numNegOnes = 0, k = 4
Output: 3
Explanation: We have a bag of items with numbers written on them {1, 1, 1, 0, 0}.
We take 3 items with 1 written on them, and 1 item with 0 written on it, and get a sum in a total of 3.
It can be proven that 3 is the maximum possible sum.

Hint 1
It is always optimal to take items with the number 1 written on them as much as possible.
Hint 2
If k > numOnes, after taking all items with the number 1,
it is always optimal to take items with the number 0 written on them as much as possible.
Hint 3
If k > numOnes + numZeroes we are forced to take k - numOnes - numZeroes -1s.
"""

# Runtime 18 ms Beats 60.27% of users with Python
# Memory 11.60 MB Beats 79.45% of users with Python

def kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k):
    """
    :type numOnes: int
    :type numZeros: int
    :type numNegOnes: int
    :type k: int
    :rtype: int
    """
    if k<=numOnes: return k
    elif k<=numOnes+numZeros: return numOnes
    else: return numOnes-(k-(numOnes+numZeros))

print(kItemsWithMaximumSum(numOnes = 6, numZeros = 6, numNegOnes = 6, k = 13))
