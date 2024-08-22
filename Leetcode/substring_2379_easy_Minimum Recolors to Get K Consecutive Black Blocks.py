"""
Done 22.08.2024. Topics: String, Sliding Window
2379. Minimum Recolors to Get K Consecutive Black Blocks
https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/description/

You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B',
representing the color of the ith block.
The characters 'W' and 'B' denote the colors white and black, respectively.

You are also given an integer k, which is the desired number of consecutive black blocks.

In one operation, you can recolor a white block such that it becomes a black block.

Return the minimum number of operations needed such that
there is at least one occurrence of k consecutive black blocks.

Example 1:
Input: blocks = "WBBWWBBWBW", k = 7
Output: 3
Explanation:
One way to achieve 7 consecutive black blocks is to recolor the 0th, 3rd, and 4th blocks
so that blocks = "BBBBBBBWBW".
It can be shown that there is no way to achieve 7 consecutive black blocks in less than 3 operations.
Therefore, we return 3.

Example 2:
Input: blocks = "WBWBBBW", k = 2
Output: 0
Explanation:
No changes need to be made, since 2 consecutive black blocks already exist.
Therefore, we return 0.

Constraints:
n == blocks.length
1 <= n <= 100
blocks[i] is either 'W' or 'B'.
1 <= k <= n

Hint 1
Iterate through all possible consecutive substrings of k characters.
Hint 2
Find the number of changes for each substring to make all blocks black,
and return the minimum of these.
"""

# Python
# Runtime 36 ms Beats 5.30%
# Memory 11.63 MB Beats 53.79%
def minimumRecolors2(blocks, k):
    """
    :type blocks: str
    :type k: int
    :rtype: int
    """
    ll=len(blocks)
    mmin = ll
    for i in range(ll):
        for j in range(i+k,ll+1):
            nw = blocks[i:j].count('W')
            if nw<mmin: mmin=nw
    return mmin


# Python 3
# Runtime 41 ms Beats 27.14%
# Memory 16.58 MB Beats 37.86%
def minimumRecolors(blocks, k):
    """
    :type blocks: str
    :type k: int
    :rtype: int
    """
    ll = len(blocks)
    mmin = ll
    for i in range(ll):
        for j in range(i + k, ll + 1):
            if (nw := blocks[i:j].count('W')) < mmin:
                mmin = nw
    return mmin


print(minimumRecolors(blocks = "WBBWWBBWBW", k = 7))
print(minimumRecolors(blocks = "WBWBBBW", k = 2))

