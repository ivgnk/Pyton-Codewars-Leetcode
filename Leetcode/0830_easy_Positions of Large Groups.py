"""
Done 04.09.2024. Topics: String
830. Positions of Large Groups
https://leetcode.com/problems/positions-of-large-groups/description/

In a string s of lowercase letters, these letters form consecutive groups of the same character.

For example, a string like s = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z", and "yy".

A group is identified by an interval [start, end], where start and end denote the start and
end indices (inclusive) of the group. In the above example, "xxxx" has the interval [3,6].

A group is considered large if it has 3 or more characters.
Return the intervals of every large group sorted in increasing order by start index.

Example 1:
Input: s = "abbxxxxzzy"
Output: [[3,6]]
Explanation: "xxxx" is the only large group with start index 3 and end index 6.

Example 2:
Input: s = "abc"
Output: []
Explanation: We have groups "a", "b", and "c", none of which are large groups.

Example 3:
Input: s = "abcdddeeeeaabbbcd"
Output: [[3,5],[6,9],[12,14]]
Explanation: The large groups are "ddd", "eeee", and "bbb".

Constraints:
1 <= s.length <= 1000
s contains lowercase English letters only.

Solution
✏️ Easy Python solution with groupby
"""

from itertools import groupby

def split_into_groups(s):
    print(len(s))
    groups = [''.join(group) for key, group in groupby(s)]
    ind=[]; i=0
    for g in groups:
        ll = len(g)
        ind.append([ll,[i,i+ll-1]])
        i+=ll
    return groups, ind

def tst_split_into_groups(s):
    # Example usage
    input_string = "aaabbbccdaa"
    groups, ind = split_into_groups(input_string)
    print(groups, ind)  # Output: ['aaa', 'bbb', 'cc', 'd', 'aa']


# Runtime 27 ms Beats 11.81%
# Memory 11.93 MB Beats 13.39%
def largeGroupPositions2(s):
    """
    :type s: str
    :rtype: List[List[int]]
    """
    ll=len(s)
    if ll<3: return []
    elif ll==3:
        if s[0]==s[1]==s[2]: return [[0,2]]
        else: return []
    else:
        groups = [''.join(group) for key, group in groupby(s)]
        ind = []; i = 0
        for g in groups:
            ll = len(g)
            ind.append([ll, [i, i + ll - 1]])
            i += ll
        return [s[1] for s in ind if s[0]>=3]


# Runtime 18 ms Beats 70.08%
# Memory 11.90 MB Beats 13.39%
def largeGroupPositions(s):
    """
    :type s: str
    :rtype: List[List[int]]
    """
    groups = [''.join(group) for key, group in groupby(s)]
    ind = [];    i = 0
    for g in groups:
        ll = len(g)
        ind.append([ll, [i, i + ll - 1]])
        i += ll
    return [s[1] for s in ind if s[0] >= 3]


print(largeGroupPositions("abbxxxxzzy"))