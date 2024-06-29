"""
Done 29.06.2024. Topics: String, Hash Table
1370. Increasing Decreasing String
https://leetcode.com/problems/increasing-decreasing-string/description/

You are given a string s. Reorder the string using the following algorithm:
1) Pick the smallest character from s and append it to the result.
2) Pick the smallest character from s which is greater than the last appended character to the result and append it.
3) Repeat step 2 until you cannot pick more characters.
4) Pick the largest character from s and append it to the result.
5) Pick the largest character from s which is smaller than the last appended character to the result and append it.
6) Repeat step 5 until you cannot pick more characters.
7) Repeat the steps from 1 to 6 until you pick all characters from s.
In each step, If the smallest or the largest character appears more than once
you can choose any occurrence and append it to the result.

Return the result string after sorting s with this algorithm.

Example 1:
Input: s = "aaaabbbbcccc"
Output: "abccbaabccba"
Explanation: After steps 1, 2 and 3 of the first iteration, result = "abc"
After steps 4, 5 and 6 of the first iteration, result = "abccba"
First iteration is done. Now s = "aabbcc" and we go back to step 1
After steps 1, 2 and 3 of the second iteration, result = "abccbaabc"
After steps 4, 5 and 6 of the second iteration, result = "abccbaabccba"

Example 2:
Input: s = "rat"
Output: "art"
Explanation: The word "rat" becomes "art" after re-ordering it with the mentioned algorithm.

Constraints:
1 <= s.length <= 500
s consists of only lowercase English letters.

Hint 1
Count the frequency of each character.
Hint 2
Loop over all character from 'a' to 'z' and append the character if it exists and decrease frequency by 1. Do the same from 'z' to 'a'.
Hint 3
Keep repeating until the frequency of all characters is zero.
"""

# Runtime 43 ms Beats 67.37%
# Memory 11.62 MB Beats 88.42%
# Runtime 40 ms Beats 75.79%
# Memory 11.68 MB Beats 88.42%
def sortString(s):
    """
    :type s: str
    :rtype: str
    """
    news=''
    dd=dict()
    for s1 in s:
        if s1 in dd:
            dd[s1]=dd[s1]+1
        else:
            dd[s1] = 1
    ind=sorted([[k,v] for k,v in dd.items()])
    ll = len(ind)
    sind = sum([ind[i][1] for i in range(ll)])
    while sind>0:
        i = 0
        while i<ll:
            if ind[i][1]>0:
                news=news+ind[i][0]
                ind[i][1]=ind[i][1]-1
                sind=sind-1
            i=i+1
        i=ll-1
        while i>-1:
            if ind[i][1]>0:
                news=news+ind[i][0]
                ind[i][1]=ind[i][1]-1
                sind = sind - 1
            i=i-1
    return news

print(sortString('aaaabbbbcccc'))
print(sortString('rat'))
