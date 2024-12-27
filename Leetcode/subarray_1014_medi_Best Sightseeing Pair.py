"""
27.12.2024. Topics: Array, Dynamic Programming
1014. Best Sightseeing Pair
https://leetcode.com/problems/best-sightseeing-pair/description/

You are given an integer array values where values[i] represents
the value of the ith sightseeing spot.
Two sightseeing spots i and j have a distance j - i between them.

The score of a pair (i < j) of sightseeing spots is values[i] + values[j] + i - j:
the sum of the values of the sightseeing spots, minus the distance between them.

Return the maximum score of a pair of sightseeing spots.

Example 1:
Input: values = [8,1,5,2,6]
Output: 11
Explanation: i = 0, j = 2, values[i] + values[j] + i - j = 8 + 5 + 0 - 2 = 11

Example 2:
Input: values = [1,2]
Output: 2

Constraints:
2 <= values.length <= 5 * 104
1 <= values[i] <= 1000

Try to think about rearranged formula,
(values[i] + i) + (values[j] - j) instead of values[i] + values[j] + i - j.
https://leetcode.com/problems/best-sightseeing-pair/description/comments/1827116

Hint 1
Can you tell the best sightseeing spot in one pass
(ie. as you iterate over the input?)
What should we store or keep track of as we iterate to do this?
"""
from typing import List


# Time Limit Exceeded - 47 / 55 testcases passed
def maxScoreSightseeingPair2(values):
    """
    :type values: List[int]
    :rtype: int
    """
    ll=len(values); rll=range(ll)
    lst_i=[values[i] + i for i in rll]
    lst_j=[values[j] - j for j in rll]
    return max(lst_i[i]+lst_j[j] for i in range(ll-1) for j in range(i+1,ll))

def maxScoreSightseeingPair3(values):
    ll=len(values); rll=range(ll)
    lst_i=sorted([(values[i] + i,i) for i in rll], reverse=True)
    lst_j=sorted([(values[j] - j,j) for j in rll], reverse=True)
    print(lst_i)
    print(lst_j)
    for i in range(ll):
        for j in range(ll):
            if lst_i[i][1]<lst_j[j][1]:
                return lst_i[i][0]+lst_j[j][0]

# Time Limit Exceeded - 47 / 55 testcases passed
def maxScoreSightseeingPair4(values: List[int]) -> int:
    ll = len(values)
    rll = range(ll)
    lst_i = [values[i] + i for i in rll]
    lst_j = [values[j] - j for j in rll]
    max_lst=[max(lst_i[:i])+lst_j[i] for i in range(1,ll)]
    return max(max_lst)

def maxScoreSightseeingPair5(values):
    ll = len(values)
    rll = range(ll)
    lst_i = [values[i] + i for i in rll]
    lst_j = [values[j] - j for j in rll]
    lst=[lst_i[0]]
    for i in range(1,ll):
        lst.append(max(lst[i-1],lst_i[i]))
    max_lst=[lst[i]+lst_j[i] for i in range(1,ll)]
    return max(max_lst)


# Runtime 52 ms Beats 91.22%
# Memory 23.24 MB Beats 20.49%
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        maxi=values[0]
        res=0
        for i in range(1,len(values)):
            maxi=maxi-1
            res=max(res,maxi+values[i])
            maxi=max(maxi,values[i])
        return res

class Solution2:
    def maxScoreSightseeingPair(self, values):
        ans = float('-inf')  # To store the maximum score
        left_max = values[0]  # Initialize left_max with the first element

        for i in range(1, len(values)):
            # Calculate the score for the current pair
            cal = values[i] + left_max - i
            # Update the maximum score
            ans = max(ans, cal)
            # Update left_max for the next iteration
            left_max = max(left_max, values[i] + i)
        return ans

class Solution3:
    def maxScoreSightseeingPair(self, values: list[int]) -> int:
        max_score = 0
        max_prev_value = values[0]  # Keeps track of the max values[i] + i seen so far

        for j in range(1, len(values)):
            # Calculate the score for the pair (i, j)
            max_score = max(max_score, max_prev_value + values[j] - j)

            # Update max_prev_value for the next iteration
            max_prev_value = max(max_prev_value, values[j] + j)

        return max_score

class Solution4:
    def maxScoreSightseeingPair(self, A):
        a, b = A[0], 0
        for i in range(1, len(A)):
            b, a = max(a + A[i] - i, b), max(A[i] + i, a)
        return b

# Example usage
values = [8, 1, 5, 2, 6]
sol = Solution()
print("Maximum Score:", sol.maxScoreSightseeingPair(values))

def maxScoreSightseeingPair(values):
    max_score = values[0] + 0
    ans = float('-inf')
    for i in range(1, len(values)):
        ans = max(ans, max_score + values[i] - i)
        max_score = max(max_score, values[i] + i)
    return ans

print(maxScoreSightseeingPair([8,1,5,2,6]))
print(maxScoreSightseeingPair([1,2]))
print(maxScoreSightseeingPair([2,2,1]))
