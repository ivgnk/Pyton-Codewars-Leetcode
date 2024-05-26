"""
Done 27.05.2024. Topics: Math
264. Ugly Number II
https://leetcode.com/problems/ugly-number-ii/description/

An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
Given an integer n, return the nth ugly number.

Example 1:
Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.

Example 2:
Input: n = 1
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.

Hint 1
The naive approach is to call isUgly for every number until you reach the nth one. Most numbers are not ugly. Try to focus your effort on generating only the ugly ones.
Hint 2
An ugly number must be multiplied by either 2, 3, or 5 from a smaller ugly number.
Hint 3
The key is how to maintain the order of the ugly numbers. Try a similar approach of merging from three sorted lists: L1, L2, and L3.
Hint 4
Assume you have Uk, the kth ugly number. Then Uk+1 must be Min(L1 * 2, L2 * 3, L3 * 5).
"""

# Runtime 86 ms Beats 73.13% of users with Python3
# Memory 16.64 MB Beats 39.91% of users with Python3

# https://leetcode.com/problems/ugly-number-ii/solutions/3235178/264-solution-with-step-by-step-explanation/
def nthUglyNumber(self, n: int) -> int:
    ugly = [1]  # initialize list of ugly numbers with 1
    i2, i3, i5 = 0, 0, 0  # initialize pointers for next multiples of 2, 3, and 5 respectively
    while len(ugly) < n:
        # generate the next ugly number as the minimum of the next multiples of 2, 3, and 5
        next_ugly = min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5)
        # add the next ugly number to the list
        ugly.append(next_ugly)
        # update the corresponding pointer for the next multiple
        if next_ugly == ugly[i2] * 2:
            i2 += 1
        if next_ugly == ugly[i3] * 3:
            i3 += 1
        if next_ugly == ugly[i5] * 5:
            i5 += 1
    return ugly[-1]  # return the nth ugly number

# Runtime 4724 ms Beats 5.03% of users with Python3
# Memory 45.21 MB Beats 5.03% of users with Python3

def nthUglyNumber(n):
    """
    :type n: int
    :rtype: int
    """
    if n <= 6: return n
    sset = set()
    if n < 100:
        n3 = n // 3 + 2
    elif n < 200:
        n3 = n // 11 + 2
    elif n < 500:
        n3 = n // 15 + 2
    else:
        n3 = n // 27 + 2
    while len(sset) < n:
        i2 = 1
        for i in range(n3):
            j3 = 1
            i2j3 = i2 * j3
            for j in range(n3):
                k5 = 1
                for k in range(n3):
                    sset.add(i2j3 * k5)
                    k5 = k5 * 5
                j3 = j3 * 3
                i2j3 = i2 * j3
            i2 = i2 * 2
    l = sorted(list(sset))
    return l[n - 1]


# Wrong Answer-- 18 / 596 testcases passed
def nthUglyNumber2(n):
    """
    :type n: int
    :rtype: int
    """
    n2=n//2
    l=[1]; l2=[2]; l3=[3]; l5=[5]
    for i in range(1,n2+2):
        l2.append(l2[-1]+2)
        l3.append(l3[-1]+3)
        l5.append(l5[-1]+5)
    print(l2)
    print(l3)
    print(l5)
    l=sorted(list(set(l+l2+l3+l5)))
    l = [i for i in l if i % 7 != 0 and i % 11 != 0]
    print(l)
    return l[n-1]

# [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
print(nthUglyNumber(1400))
# print(nthUglyNumber(18))