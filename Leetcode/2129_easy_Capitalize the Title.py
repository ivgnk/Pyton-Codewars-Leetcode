"""
2129. Capitalize the Title
https://leetcode.com/problems/capitalize-the-title/description/

You are given a string title consisting of one or more words separated by a single space,
where each word consists of English letters.
Capitalize the string by changing the capitalization of each word such that:
If the length of the word is 1 or 2 letters, change all letters to lowercase.
Otherwise, change the first letter to uppercase and the remaining letters to lowercase.
Return the capitalized title.

Example 1:
Input: title = "capiTalIze tHe titLe"
Output: "Capitalize The Title"
Explanation:
Since all the words have a length of at least 3, the first letter of each word is uppercase, and the remaining letters are lowercase.

Example 2:
Input: title = "First leTTeR of EACH Word"
Output: "First Letter of Each Word"
Explanation:
The word "of" has length 2, so it is all lowercase.
The remaining words have a length of at least 3, so the first letter of each remaining word is uppercase, and the remaining letters are lowercase.

Example 3:
Input: title = "i lOve leetcode"
Output: "i Love Leetcode"
Explanation:
The word "i" has length 1, so it is lowercase.
The remaining words have a length of at least 3, so the first letter of each remaining word is uppercase, and the remaining letters are lowercase.
"""

# Runtime 11 ms Beats 81.55% of users with Python
# Memory 11.85 MB Beats 11.90% of users with Python

def capitalizeTitle(title):
    """
    :type title: str
    :rtype: str
    """
    s=title.split()
    for i in range(len(s)):
        if len(s[i])==1 or len(s[i])==2: s[i]=s[i].lower()
        else: s[i]=s[i].capitalize()
    return ' '.join(s)

print(capitalizeTitle(title = "capiTalIze tHe titLe"))
print(capitalizeTitle(title = "First leTTeR of EACH Word"))
