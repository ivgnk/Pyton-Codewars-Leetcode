"""
Done 12.05.2024. Topics: String
3136. Valid Word
A word is considered valid if:

It contains a minimum of 3 characters.
It contains only digits (0-9), and English letters (uppercase and lowercase).
It includes at least one vowel.
It includes at least one consonant.
You are given a string word.

Return true if word is valid, otherwise, return false.
Notes:
'a', 'e', 'i', 'o', 'u', and their uppercases are vowels.
A consonant is an English letter that is not a vowel.

Example 1:
Input: word = "234Adas"
Output: true
Explanation:
This word satisfies the conditions.

Example 2:
Input: word = "b3"
Output: false
Explanation:
The length of this word is fewer than 3, and does not have a vowel.

Example 3:
Input: word = "a3$e"
Output: false
Explanation:
This word contains a '$' character and does not have a consonant.
"""

a_l2='bcdfghjklmnpqrstvwxyz'
vowel2=['a', 'e', 'i', 'o', 'u']
num=['0','1','2','3','4','5','6','7','8','9']
bad=['$','#','@']

# Runtime 18 ms Beats 38.89% of users with Python
# Memory 11.43 MB Beats 99.66% of users with Python
# Runtime 16 ms Beats 55.72% of users with Python
# Memory 11.63 MB Beats 57.91% of users with Python
# Runtime 14 ms Beats 70.20% of users with Python
# Memory 11.68 MB Beats 57.91% of users with Python
def isValid2(word):
    """
    :type word: str
    :rtype: bool
    """
    word=word.lower()
    ll=len(word)
    if ll<3: return False
    # if not any([True if w in num else False for w in word]): return False
    if not any([True if w in vowel2 else False for w in word]): return False
    if not any([True if w in a_l2 else False for w in word]): return False
    return True

a_l='bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
vowel=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

# Runtime 18 ms Beats 38.89% of users with Python
# Memory 11.57 MB Beats 87.37% of users with Python
# Runtime 17 ms Beats 44.61% of users with Python
# Memory 11.68 MB Beats 57.91% of users with Python
def isValid2(word):
    """
    :type word: str
    :rtype: bool
    """
    ll=len(word)
    if ll<3: return False
    # if not any([True if w in num else False for w in word]): return False
    if not any([True if w in vowel else False for w in word]): return False
    if not any([True if w in a_l else False for w in word]): return False
    return True

print(isValid("UuE6"))
