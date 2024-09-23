"""
23.09.2024. Topics: Dynamic Programming
2707. Extra Characters in a String
https://leetcode.com/problems/extra-characters-in-a-string

You are given a 0-indexed string s and a dictionary of words dictionary.
You have to break s into one or more non-overlapping substrings such that each substring is present in dictionary.
There may be some extra characters in s which are not present in any of the substrings.
Return the minimum number of extra characters left over if you break up s optimally.

Example 1:
Input: s = "leetscode", dictionary = ["leet","code","leetcode"]
Output: 1
Explanation: We can break s in two substrings: "leet" from index 0 to 3 and "code" from index 5 to 8. There is only 1 unused character (at index 4), so we return 1.

Example 2:
Input: s = "sayhelloworld", dictionary = ["hello","world"]
Output: 3
Explanation: We can break s in two substrings: "hello" from index 3 to 7 and "world" from index 8 to 12. The characters at indices 0, 1, 2 are not used in any substring and thus are considered as extra characters. Hence, we return 3.

Constraints:
1 <= s.length <= 50
1 <= dictionary.length <= 50
1 <= dictionary[i].length <= 50
dictionary[i] and s consists of only lowercase English letters
dictionary contains distinct words

Hint 1
Can we use Dynamic Programming here?
Hint 2
Define DP[i] as the min extra character if breaking up s[0:i] optimally.

Tip1
Knapsack problem

I think description should mention, we are allowed to reuse the dictionary word multiple time.
https://leetcode.com/problems/extra-characters-in-a-string/description/comments/2040417
"""
from icecream import ic

# https://leetcode.com/problems/extra-characters-in-a-string/solutions/5822528/extra-character-in-a-string/
def minExtraChar(s, dictionary):
    wordSet = set(dictionary)
    n = len(s)
    dp = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        dp[i] = dp[i + 1] + 1
        ic(i,dp[i],dp[0])
        for length in range(1, n - i + 1):
            ic(i,s[i:i + length])
            if s[i:i + length] in wordSet:
                dp[i] = min(dp[i], dp[i + length])
                ic(length, s[i:i + length], i, dp[i])
    return dp[0]

ic(minExtraChar(s = "dwmodizxvvbosxxw",
                dictionary = ["ox","lb","diz","gu","v","ksv","o","nuq","r","txhe","e","wmo","cehy","tskz","ds","kzbu"]))


# Wrong Answer - # 1336 / 2028 testcases passed
# s = "dwmodizxvvbosxxw" dictionary =
# ["ox","lb","diz","gu","v","ksv","o","nuq","r","txhe","e","wmo","cehy","tskz","ds","kzbu"]
# Output 9
# Expected 7

def minExtraChar2(s, dictionary):
    """
    :type s: str
    :type dictionary: List[str]
    :rtype: int
    """
    dd=list(set(dictionary))
    ls=len(s)
    lw = len(dd)
    lwall = [len(word) for word in dd]
    Tr = [True] * lw
    while any(Tr):
        for i, word in enumerate(dd):
            Tr[i] = word in s
            if Tr[i]:
                s = s.replace(word, ' ' * lwall[i])
    s=s.replace(' ','')
    return ls-len(s)

# https://leetcode.com/problems/extra-characters-in-a-string/solutions/5824415/brute-backtracking-memoization-dp/
def minExtraChar3(s, dictionary):
    """
    :type s: str
    :type dictionary: List[str]
    :rtype: int
    """
    n = len(s)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0  # Base case: no characters, no extra chars

    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + 1
        for word in set(dictionary):
            word_len = len(word)
            if i >= word_len and s[i - word_len:i] == word:
                dp[i] = min(dp[i], dp[i - word_len])
        ic(i,dp[i],)
    return dp[n]

