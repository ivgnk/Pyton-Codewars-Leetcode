'''
Done 22.09.2024. Topics: Array, String
1528. Shuffle String
You are given a string s and an integer array indices of the same length.
The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.
Return the shuffled string.

Example 1:
Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.

Example 2:
Input: s = "abc", indices = [0,1,2]
Output: "abc"
Explanation: After shuffling, each character remains in its position.
'''

# Even 1 test case is incorrect

from icecream import ic
def restoreString_(s, indices):
    """
    :type s: str
    :type indices: List[int]
    :rtype: str
    """
    # for i in range(len(s)):
    #     print(s[indices[i]])
    s2 = ''.join([s[indices[i]] for i in range(len(s))])
    return s2


# Runtime 56 ms Beats 11.86%
# Memory 11.81 MB Beats 6.48%
def restoreString2(s, indices):
    """
    :type s: str
    :type indices: List[int]
    :rtype: str
    """
    # for i in range(len(s)):
    #     print(s[indices[i]])
    n = len(s)
    rn = range(n)
    lst=[' ' for _ in rn]
    for i in rn:
        lst[indices[i]]=s[i]
    return ''.join(lst)

# Runtime 61 ms Beats 7.31%
# Memory 11.64 MB Beats 60.69%
def restoreString(s, indices):
    return ''.join([c for i, c in sorted(zip(indices, s))])


ic(restoreString(s = "codeleet", indices = [4,5,6,7,0,2,1,3]))
# ic(restoreString(s = "aiohn" , indices = [3,1,4,2,0]))

#------ Not work
def restoreString(s, indices):
    """
    :type s: str
    :type indices: List[int]
    :rtype: str
    """
    s2 = ''.join([s[indices[i]] for i in range(len(s))])
    return s2
