"""
Done 27.05.2024. Topics: String
1704. Determine if String Halves Are Alike
https://leetcode.com/problems/determine-if-string-halves-are-alike/description/

You are given a string s of even length.
Split this string into two halves of equal lengths,
and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels
('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U').
Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.

Example 1:
Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.

Example 2:
Input: s = "textbook"
Output: false
Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
Notice that the vowel o is counted twice.

Hint 1
Create a function that checks if a character is a vowel, either uppercase or lowercase.
"""

# Runtime 24 ms Beats 35.28% of users with Python
# Memory 11.59 MB Beats 94.44% of users with Python

vowel_low = ['a', 'e', 'i', 'o', 'u']
def halvesAreAlike(s):
    """
    :type s: str
    :rtype: bool
    """
    s=s.lower()
    ll=len(s)//2
    s1=s[:ll]; s2=s[ll:]
    return sum([ss in vowel_low for ss in s1])==sum([ss in vowel_low for ss in s2])


print(halvesAreAlike("book"))



