'''
Re-solution 09.05.2024. Topics: Array, Sorting, Heap (Priority Queue)
506. Relative Ranks
https://leetcode.com/problems/relative-ranks/description/

You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition.
All the scores are guaranteed to be unique.

The athletes are placed based on their scores, where the 1st place athlete has the highest score,
the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

The 1st place athlete's rank is "Gold Medal".
The 2nd place athlete's rank is "Silver Medal".
The 3rd place athlete's rank is "Bronze Medal".
For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
Return an array answer of size n where answer[i] is the rank of the ith athlete.

Example 1:
Input: score = [5,4,3,2,1]
Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].

Example 2:
Input: score = [10,3,8,9,4]
Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
Explanation: The placements are [1st, 5th, 3rd, 2nd, 4th].
'''


# Runtime 246 ms Beats 26.73% of users with Python3
# Memory 17.77 MB Beats 49.94% of users with Python3

def findRelativeRanks2(score):
    """
    :type score: List[int]
    :rtype: List[str]
    """
    print(f'{score=}')
    sc_sort = sorted(score, reverse=True)
    the_ind = [sc_sort.index(s) for s in score]
    sc_dict = dict(zip(score,the_ind)) # https://builtin.com/software-engineering-perspectives/convert-list-to-dictionary-python
    res = []
    for value1 in sc_dict:
        value = sc_dict[value1]
        if value==0: res.append("Gold Medal")
        elif value==1: res.append("Silver Medal")
        elif value==2: res.append("Bronze Medal")
        else: res.append(str(value+1))
    return res

# Runtime 246 ms Beats 26.73% of users with Python3
# Memory 17.77 MB Beats 49.94% of users with Python3
def findRelativeRanks(score):
    """
    :type score: List[int]
    :rtype: List[str]
    """
    sc_sort = sorted(score, reverse=True)
    the_ind = [sc_sort.index(s) for s in score]
    res = []
    for i in range(len(score)):
        value = the_ind[i]
        if value==0: res.append("Gold Medal")
        elif value==1: res.append("Silver Medal")
        elif value==2: res.append("Bronze Medal")
        else: res.append(str(value+1))
    return res

# Runtime 242 ms Beats 27.26% of users with Python3
# Memory 17.74 MB Beats 49.94% of users with Python3
def findRelativeRanks(score):
    sc_sort = sorted(score, reverse=True)
    the_ind = [sc_sort.index(s) for s in score]
    res = []
    for i in the_ind:
        if i == 0:        res.append("Gold Medal")
        elif i == 1:      res.append("Silver Medal")
        elif i == 2:      res.append("Bronze Medal")
        else:  res.append(str(i + 1))
    return res

print(findRelativeRanks([5,4,3,2,1]))
print(findRelativeRanks([10,3,8,9,4]))