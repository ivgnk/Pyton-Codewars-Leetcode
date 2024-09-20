"""
Done 20.09.2024. Topics: String
824. Goat Latin
https://leetcode.com/problems/goat-latin/description/

You are given a string sentence that consist of words separated by spaces.
Each word consists of lowercase and uppercase letters only.

We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)
The rules of Goat Latin are as follows:

If a word begins with a vowel ('a', 'e', 'i', 'o', or 'u'), append "ma" to the end of the word.
For example, the word "apple" becomes "applema".
If a word begins with a consonant (i.e., not a vowel), remove the first letter and append it to the end, then add "ma".
For example, the word "goat" becomes "oatgma".
Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
For example, the first word gets "a" added to the end, the second word gets "aa" added to the end, and so on.
Return the final sentence representing the conversion from sentence to Goat Latin.

Example 1:
Input: sentence = "I speak Goat Latin"
Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"

Example 2:
Input: sentence = "The quick brown fox jumped over the lazy dog"
Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"

Constraints:
1 <= sentence.length <= 150
sentence consists of English letters and spaces.
sentence has no leading or trailing spaces.
All the words in sentence are separated by a single space.
"""

# Runtime 13 ms Beats 63.24%
# Memory 11.55 MB Beats 95.26%
# Runtime 8 ms Beats 94.07%
# Memory 11.65 MB Beats 73.91%
vow=['a', 'e', 'i', 'o', 'u',
     'A', 'E', 'I', 'O', 'U']
def toGoatLatin(sentence):
    """
    :type sentence: str
    :rtype: str
    """
    s=sentence.split()
    for i in range(len(s)):
        if s[i][0] not in vow:
            s[i] = s[i][1:]+s[i][0]
        s[i] +='ma'+'a'*(i+1)
    return ' '.join(s)

print(toGoatLatin("I speak Goat Latin"))