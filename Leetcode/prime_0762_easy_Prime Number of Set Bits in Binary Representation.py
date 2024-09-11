"""
Done 11.09.2024. Topics: Math, Bit Manipulation
762. Prime Number of Set Bits in Binary Representation
https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/description/

Given two integers left and right, return the count of numbers in the inclusive range [left, right]
having a prime number of set bits in their binary representation.

Recall that the number of set bits an integer has is the number of 1's present when written in binary.
For example, 21 written in binary is 10101, which has 3 set bits.

Example 1:
Input: left = 6, right = 10
Output: 4
Explanation:
6  -> 110 (2 set bits, 2 is prime)
7  -> 111 (3 set bits, 3 is prime)
8  -> 1000 (1 set bit, 1 is not prime)
9  -> 1001 (2 set bits, 2 is prime)
10 -> 1010 (2 set bits, 2 is prime)
4 numbers have a prime number of set bits.

Example 2:
Input: left = 10, right = 15
Output: 5
Explanation:
10 -> 1010 (2 set bits, 2 is prime)
11 -> 1011 (3 set bits, 3 is prime)
12 -> 1100 (2 set bits, 2 is prime)
13 -> 1101 (3 set bits, 3 is prime)
14 -> 1110 (3 set bits, 3 is prime)
15 -> 1111 (4 set bits, 4 is not prime)
5 numbers have a prime number of set bits.

Constraints:
1 <= left <= right <= 106
0 <= right - left <= 104

Hint 1
Write a helper function to count the number of set bits in a number,
then check whether the number of set bits is 2, 3, 5, 7, 11, 13, 17 or 19.
"""

# Runtime 140 ms Beats 75.58%
# Memory 12.24 MB Beats 9.30%
# Time Complexity O(N)
# Space Complexity O(1)

pr = [2, 3, 5, 7, 11, 13, 17, 19]
def countPrimeSetBits(left, right):
    """
    :type left: int
    :type right: int
    :rtype: int
    """
    n = [bin(i)[2:] for i in range(left, right+1)]
    n2 = [s.count('1') for s in n]
    return sum([s in pr for s in n2])

print(countPrimeSetBits(6,10))
print(countPrimeSetBits(10,15))

