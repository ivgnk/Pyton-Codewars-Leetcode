"""
Done 01.10.2024. Topics: Hash Table
Topics: Array, Hash Table, Counting
1497. Check If Array Pairs Are Divisible by k
https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/description
Given an array of integers arr of even length n and an integer k.

We want to divide the array into exactly n / 2 pairs such that the sum of each pair is divisible by k.

Return true If you can find a way to do that or false otherwise.

Example 1:

Input: arr = [1,2,3,4,5,10,6,7,8,9], k = 5
Output: true
Explanation: Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).
Example 2:

Input: arr = [1,2,3,4,5,6], k = 7
Output: true
Explanation: Pairs are (1,6),(2,5) and(3,4).
Example 3:

Input: arr = [1,2,3,4,5,6], k = 10
Output: false
Explanation: You can try all possible pairs to see that there is no way to divide arr
into 3 pairs each with sum divisible by 10.

Constraints:
arr.length == n
1 <= n <= 105
n is even.
-109 <= arr[i] <= 109
1 <= k <= 105

Hint 1
Keep an array of the frequencies of ((x % k) + k) % k for each x in arr.
Hint 2
for each i in [0, k - 1] we need to check if freq[i] == freq[k - i]
Hint 3
Take care of the case when i == k - i and when i == 0

My solution
https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/solutions/5854921/python-solution-based-on-dictionary-and-hints/
✏️ Python solution based on dictionary and hints

# Intuition
1. Preliminary control of whole array for %k!=0
2. Preliminary preparation of dict based on hint 1
3. Main control based on hint 2 and 3

# Approach
- "array of the frequencies" is dictionary
- "array of the frequencies" is not list
"""

# Runtime 518 ms Beats 64.29%
# Memory 32.90 MB Beats 5.36%
from icecream import ic
def canArrange(arr, k):
    """
    :type arr: List[int]
    :type k: int
    :rtype: bool
    """
    # https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/description/comments/1573985
    # if a some part of array get divisible by some k , the whole sum of the array must and

    # 1. Preliminary control
    if len(set(arr)) == 1:
        return arr[0] % k == 0
    if sum(arr)%k!=0: return False

    # fr=[((a1% k) + k)% k for a1 in arr]
    # arr: [1, 2, 3, 4, 5, 10, 6, 7, 8, 9]
    # ic| fr: [1, 2, 3, 4, 0, 0, 1, 2, 3, 4]

    # 2. Preliminary preparation of dict based on hint 1
    dd=dict()
    for a1 in arr:
        d=((a1% k) + k)% k
        if d in dd:
            dd[d]+=1
        else:
            dd[d] = 1
    ic(dd)
    # 3. Main control based on hint 2 and 3
    for key,val in dd.items():
        if key==0:
            if dd[key]%2!=0: return False
        else:
            if k-key not in dd: return False
            if dd[key]!=dd[k-key]: return False
    return True
# ic(canArrange(arr = [1,2,3,4,5,10,6,7,8,9], k = 5)) #True
# ic(canArrange([1,2,3,4,5,6], k = 7)) #True
# ic(canArrange(arr = [1,2,3,4,5,6], k = 10)) #False
# ic(canArrange(arr = [5,5,1,2,3,4], k = 10)) # False
ic(canArrange(arr = [2,2,2,2,2,2], k = 3))

# Wrong Answer - 93 / 97 testcases passed
def canArrange2(arr, k):
    """
    :type arr: List[int]
    :type k: int
    :rtype: bool
    """
    # https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/description/comments/1573985
    # if a some part of array get divisible by some k , the whole sum of the array must and
    if len(set(arr)) == 1:
        return sum(arr) % k == 0
    return sum(arr) % k == 0




