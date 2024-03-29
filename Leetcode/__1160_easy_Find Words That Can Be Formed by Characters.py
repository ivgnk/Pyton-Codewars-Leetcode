'''
1160. Find Words That Can Be Formed by Characters
https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

You are given an array of strings words and a string chars.
A string is good if it can be formed by characters from chars (each character can only be used once).
Return the sum of lengths of all good strings in words.


Example 1:
Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

Example 2:
Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
'''

# Wrong Answer 10 / 36 testcases passed
# Super long words and a list

def countCharacters(words, chars):
    """
    :type words: List[str]
    :type chars: str
    :rtype: int
    """
    ssum=0
    for s in words:
        Tr=True
        for s1 in s:
            Tr=Tr and (s1 in chars)
        if Tr:
            ssum=ssum+len(s)
    return ssum

print(countCharacters(words = ["cat","bt","hat","tree"], chars = "atach"))
print(countCharacters( words = ["hello","world","leetcode"], chars = "welldonehoneyr"))