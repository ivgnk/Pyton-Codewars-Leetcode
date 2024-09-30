"""
Done 30.09.2024. Topics: Binary Search
278. First Bad Version
https://leetcode.com/problems/first-bad-version/description/

You are a product manager and currently leading a team to develop a new product.
Unfortunately, the latest version of your product fails the quality check.
Since each version is developed based on the previous version,
all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,
which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad.
Implement a function to find the first bad version.
You should minimize the number of calls to the API.

Example 1:
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

Example 2:
Input: n = 1, bad = 1
Output: 1

Constraints:
1 <= bad <= n <= 2**31 - 1

Solution
✏️ Python solution with binary search and a special function for it
# Intuition
To binary search work properly,
you need a special function to detect when the desired (bad) version appears.
"""

# The isBadVersion API is already defined for you.
bad_=1_702_766_719
n_ = 2126753390

from icecream import ic
def isBadVersion(version: int) -> bool:
    return version>=bad_

# Time Limit Exceeded -  11 / 24 testcases passed
# submitted at Apr 03, 2024 14:55
# n = 2126753390, bad = 1702766719
def firstBadVersion2(n: int) -> int:
    first=isBadVersion(1)
    if first: return 1
    for i in range(2,n+1):
        if isBadVersion(i) != first:
            return i

# Runtime 8 ms Beats 87.39%
# Memory 11.44 MB Beats 90.58%
class Solution:
    def dbl_find(self,n):
        return isBadVersion(n), isBadVersion(n-1)

    def firstBadVersion(self, n):
        if isBadVersion(1): return 1
        # if self.dbl_find(n): return n
        return self.binary_search(1, n)

    # https://www.geeksforgeeks.org/python-program-for-binary-search/
    # https://www.geeksforgeeks.org/binary-search-bisect-in-python/
    # https://docs.python.org/3/library/bisect.html
    def binary_search(self, low, high):
        # Check base case
        mid = 0
        if high >= low:
            mid = (high + low) // 2
            # If element is present at the middle itself
            m,mp=self.dbl_find(mid)
            # print('{0:,}'.format(mid).replace(',', ' '), m, mp)
            if m and not mp: return mid
            if not m and not mp:
                return self.binary_search(mid + 1, high)
            # Else the element can only be present in right subarray
            else:
                return self.binary_search(low, mid-1)

obj = Solution()
d=obj.firstBadVersion(n_)
print('result = {0:,}'.format(d).replace(',', ' '))

# ic(obj.dbl_find(2))
# ic(obj.dbl_find(bad_-1))
# ic(obj.dbl_find(bad_))
# ic(obj.dbl_find(bad_+1))
# ic(obj.dbl_find(n_))