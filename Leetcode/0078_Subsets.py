'''
Given an integer array nums of unique elements, return all possible
subsets.
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
'''

# Генерация всех перестановок списка в Python
# https://sky.pro/media/generacziya-vseh-perestanovok-spiska-v-python/

import itertools


def subsets(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    llen = len(nums)
    rlst=[[]]
    for dat in nums: rlst.append([dat])
    # https://stackoverflow.com/questions/464864/get-all-possible-2n-combinations-of-a-list-s-elements-of-any-length
    for L in range(2, llen + 1):
        for subset in itertools.combinations(nums, L):
            rlst.append(list(subset))

    return rlst

print(subsets([1,2,3]))

