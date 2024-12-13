"""
13.12.2024. Topics: Sorting
2593. Find Score of an Array After Marking All Elements
https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/

You are given an array nums consisting of positive integers.

Starting with score = 0, apply the following algorithm:

Choose the smallest integer of the array that is not marked.
If there is a tie, choose the one with the smallest index.
Add the value of the chosen integer to score.
Mark the chosen element and its two adjacent elements if they exist.
Repeat until all the array elements are marked.
Return the score you get after applying the above algorithm.

Example 1:
Input: nums = [2,1,3,4,5,2]
Output: 7
Explanation: We mark the elements as follows:
- 1 is the smallest unmarked element, so we mark it and its two adjacent elements: [2,1,3,4,5,2].
- 2 is the smallest unmarked element, so we mark it and its left adjacent element: [2,1,3,4,5,2].
- 4 is the only remaining unmarked element, so we mark it: [2,1,3,4,5,2].
Our score is 1 + 2 + 4 = 7.

Example 2:
Input: nums = [2,3,5,1,3,2]
Output: 5
Explanation: We mark the elements as follows:
- 1 is the smallest unmarked element, so we mark it and its two adjacent elements: [2,3,5,1,3,2].
- 2 is the smallest unmarked element, since there are two of them, we choose the left-most one, so we mark the one at index 0 and its right adjacent element: [2,3,5,1,3,2].
- 2 is the only remaining unmarked element, so we mark it: [2,3,5,1,3,2].
Our score is 1 + 2 + 2 = 5.

Constraints:
1 <= nums.length <= 105
1 <= nums[i] <= 106

Hint 1
Try simulating the process of marking the elements and their adjacent.
Hint 2
If there is an element that was already marked, then you skip it.
"""
# https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/editorial
# Runtime 343 ms Beats 82.91%
# Memory 36.42 MB Beats 88.42%
def findScore(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    score = 0; ll=len(nums)
    srt = [(num, i) for i, num in enumerate(nums)]
    srt.sort()
    mark = [False] * ll
    print(srt)
    for i in range(len(nums)):
        number = srt[i][0]
        ind = srt[i][1]
        if not mark[ind]:
            score += number
            mark[ind] = True
            # mark adjacent elements if they exist
            if ind - 1 >= 0:
                mark[ind - 1] = True
            if ind + 1 < ll:
                mark[ind + 1] = True
    return score


if __name__=="__main__":
    print(findScore(nums = [2,1,3,4,5,2]))
