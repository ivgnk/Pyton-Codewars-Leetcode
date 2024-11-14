"""
14.11.2024. Topics: Binary Search
2064. Minimized Maximum of Products Distributed to Any Store
https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store

You are given an integer n indicating there are n specialty retail stores.
There are m product types of varying amounts,
which are given as a 0-indexed integer array quantities,
where quantities[i] represents the number of products of the ith product type.

You need to distribute all products to the retail stores following these rules:

A store can only be given at most one product type but can be given any amount of it.
After distribution, each store will have been given some number of products (possibly 0).
Let x represent the maximum number of products given to any store.
You want x to be as small as possible, i.e.,
you want to minimize the maximum number of products that are given to any store.
Return the minimum possible x.

Example 1:
Input: n = 6, quantities = [11,6]
Output: 3
Explanation: One optimal way is:
- The 11 products of type 0 are distributed to the first four stores in these amounts: 2, 3, 3, 3
- The 6 products of type 1 are distributed to the other two stores in these amounts: 3, 3
The maximum number of products given to any store is max(2, 3, 3, 3, 3, 3) = 3.

Example 2:
Input: n = 7, quantities = [15,10,10]
Output: 5
Explanation: One optimal way is:
- The 15 products of type 0 are distributed to the first three stores in these amounts: 5, 5, 5
- The 10 products of type 1 are distributed to the next two stores in these amounts: 5, 5
- The 10 products of type 2 are distributed to the last two stores in these amounts: 5, 5
The maximum number of products given to any store is max(5, 5, 5, 5, 5, 5, 5) = 5.
Example 3:

Input: n = 1, quantities = [100000]
Output: 100000
Explanation: The only optimal way is:
- The 100000 products of type 0 are distributed to the only store.
The maximum number of products given to any store is max(100000) = 100000.

Constraints:
m == quantities.length
1 <= m <= n <= 105
1 <= quantities[i] <= 105

Hint 1
There exists a monotonic nature such that when x is smaller than some number,
there will be no way to distribute, and when x is not smaller than that number,
there will always be a way to distribute.
Hint 2
If you are given a number k, where the number of products given to any store does not exceed k,
could you determine if all products can be distributed?
Hint 3
Implement a function canDistribute(k),
which returns true if you can distribute all products such that any store will not be given
more than k products, and returns false if you cannot.
Use this function to binary search for the smallest possible k.

# https://leetcode.com/discuss/general-discussion/786126/Python-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems
"""

# Wrong Answer - 120 / 219 testcases passed
from math import ceil
from bisect import bisect_left
from typing import List


def minimizedMaximum2(n, quantities):
    """
    :type n: int
    :type quantities: List[int]
    :rtype: int
    """
    if n==len(quantities):  return max(quantities)
    return ceil(sum(quantities)/n)

# https://github.com/doocs/leetcode/blob/main/solution/2000-2099/2064.Minimized%20Maximum%20of%20Products%20Distributed%20to%20Any%20Store/README_EN.md
# https://algo.monster/liteproblems/2064
class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def check(x):
            return sum((v + x - 1) // x for v in quantities) <= n
        return 1 + bisect_left(range(1, 10**6), True, key=check)

# https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/solutions/6030158/conditional-based-binary-search
class Solution2:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        # Condition Based Binary Search
        l, r = 1, max(quantities)
        while l < r:
            k = (l + r) // 2
            if sum(ceil(i / k) for i in quantities) <= n:
                r = k  # since this k return true
            else:
                l = k + 1  # since this k returns false

        return l


if __name__=="__main__":
    # print(minimizedMaximum(n = 6, quantities = [11,6]))
    # print(minimizedMaximum(n = 7, quantities = [15,10,10]))
    # print(minimizedMaximum(n = 1, quantities = [100000]))
    # print(minimizedMaximum(n = 2, quantities = [5,7]))
    # print(minimizedMaximum(n = 22, quantities = [25, 11, 29, 6, 24, 4, 29, 18, 6, 13, 25, 30]))
    # print(minimizedMaximum(n = 7, quantities = [100000,100000,100000,100000,100000,100000,100000]))
    ...