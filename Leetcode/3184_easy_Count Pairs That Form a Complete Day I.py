"""
Done 28.06.2024. Topics: Array, Hash Table
3184. Count Pairs That Form a Complete Day I
https://leetcode.com/problems/count-pairs-that-form-a-complete-day-i/description/

Given an integer array hours representing times in hours, return an integer denoting the number of pairs i, j where
i < j and hours[i] + hours[j] forms a complete day.
A complete day is defined as a time duration that is an exact multiple of 24 hours.
For example, 1 day is 24 hours, 2 days is 48 hours, 3 days is 72 hours, and so on.

Example 1:
Input: hours = [12,12,30,24,24]
Output: 2
Explanation:
The pairs of indices that form a complete day are (0, 1) and (3, 4).
Example 2:
Input: hours = [72,48,24,3]
Output: 3
Explanation:
The pairs of indices that form a complete day are (0, 1), (0, 2), and (1, 2).

Hint 1
Brute force all pairs (i, j) and check if they form a valid complete day.
It is considered a complete day if (hours[i] + hours[j]) % 24 == 0.
"""

# Runtime 48 ms Beats 20.95%
# Memory 11.70 MB Beats 23.09%
def countCompleteDayPairs3(hours):
    """
    :type hours: List[int]
    :rtype: int
    """
    ll=len(hours)
    return sum([(hours[i] + hours[j]) % 24 == 0  for i in range(ll) for j in range(i+1,ll)])

# Runtime 46 ms Beats 28.36%
# Memory 11.55 MB Beats 56.82%
# Runtime 42 ms Beats 46.29%
# Memory 11.69 MB Beats 23.09%
def countCompleteDayPairs2(self, hours):
    """
    :type hours: List[int]
    :rtype: int
    """
    return sum([(hours[i] + hours[j]) % 24 == 0 for i in range(len(hours)) for j in range(i + 1, len(hours))])

# Runtime 39 ms Beats 56.61%
# Memory 11.53 MB Beats 56.82%
# Runtime 29 ms Beats 80.02%
# Memory 11.32 MB Beats 97.74%
def countCompleteDayPairs(hours):
    """
    :type hours: List[int]
    :rtype: int
    """
    score = 0
    for i in range(len(hours)):
        for j in range(i + 1, len(hours)):
            if (hours[i] + hours[j]) % 24 == 0:
                score += 1
    return score

