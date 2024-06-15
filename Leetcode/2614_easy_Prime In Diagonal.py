"""
Done 15.06.2024. Topics: Array, Math, Matrix, Number Theory
2614. Prime In Diagonal
https://leetcode.com/problems/prime-in-diagonal/description/

You are given a 0-indexed two-dimensional integer array nums.
Return the largest prime number that lies on at least one of the diagonals of nums.
In case, no prime is present on any of the diagonals, return 0.

Note that:
An integer is prime if it is greater than 1 and has no positive integer divisors other than 1 and itself.
An integer val is on one of the diagonals of nums if there exists an integer i for which nums[i][i] = val
or an i for which nums[i][nums.length - i - 1] = val.

In the above diagram, one diagonal is [1,5,9] and another diagonal is [3,5,7].

Example 1:
Input: nums = [[1,2,3],[5,6,7],[9,10,11]]
Output: 11
Explanation: The numbers 1, 3, 6, 9, and 11 are the only numbers present on at least one of the diagonals.
Since 11 is the largest prime, we return 11.

Example 2:
Input: nums = [[1,2,3],[5,17,7],[9,11,10]]
Output: 17
Explanation: The numbers 1, 3, 9, 10, and 17 are all present on at least one of the diagonals.
17 is the largest prime, so we return 17.

Hint 1
Iterate over the diagonals of the matrix and check for each element.
Hint 2
Check if the element is prime or not in O(sqrt(n)) time.
"""

# Runtime 1452 ms Beats 5.18%
# Memory 65.67 MB Beats 5.40%

from math import isqrt
def list_of_primes_less_n(n):
    isq=isqrt(n)
    a=[True]*n
    for i in range(2,isq+1):
        if a[i]==True:
            j=0; nn=i**2
            while j<n:
                if nn <n:
                    a[nn]=False
                    j=j+1
                    nn=nn+i
                else: break
    return [i for i in range(2,n) if a[i]]

def diagonalPrime2(nums):
    """
    :type nums: List[List[int]]
    :rtype: int
    """
    ll=len(nums); rll=range(ll)
    lst1=[nums[i][i] for i in rll]
    lst2=[nums[-1-i][i] for i in rll]
    lst=sorted(set(lst1+lst2),reverse=True)
    mmax=max(lst)
    prm_lst=list_of_primes_less_n(mmax+1)
    for i in range(len(lst)):
        if lst[i] in prm_lst: return lst[i]
    else: return 0


# Runtime 566 ms Beats 90.06%
# Memory 28.45 MB Beats 81.21%
# https://leetcode.com/problems/prime-in-diagonal/solutions/5106844/its-simple-with-steps-simple-to-understand/
def is_prime(n):
        """Check if a number is prime."""
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

def diagonalPrime(nums):
    """
    :type nums: List[List[int]]
    :rtype: int
    """
    ll=len(nums); rll=range(ll)
    lst1=[nums[i][i] for i in rll]
    lst2=[nums[-1-i][i] for i in rll]
    lst=sorted(set(lst1+lst2),reverse=True)
    for i in range(len(lst)):
        if is_prime(lst[i]): return lst[i]
    else: return 0

print(diagonalPrime([[1,2,3],[5,6,7],[9,10,11]]))