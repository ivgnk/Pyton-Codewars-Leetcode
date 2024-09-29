"""
Done 29.09.2024. Topics: String
2490. Circular Sentence
https://leetcode.com/problems/circular-sentence/description/

A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
For example, "Hello World", "HELLO", "hello world hello world" are all sentences.
Words consist of only uppercase and lowercase English letters.
Uppercase and lowercase English letters are considered different.

A sentence is circular if:
The last character of a word is equal to the first character of the next word.
The last character of the last word is equal to the first character of the first word.
For example, "leetcode exercises sound delightful", "eetcode", "leetcode eats soul" are all circular sentences.
However, "Leetcode is cool", "happy Leetcode", "Leetcode" and "I like Leetcode" are not circular sentences.

Given a string sentence, return true if it is circular. Otherwise, return false.

Example 1:
Input: sentence = "leetcode exercises sound delightful"
Output: true
Explanation: The words in sentence are ["leetcode", "exercises", "sound", "delightful"].
- leetcode's last character is equal to exercises's first character.
- exercises's last character is equal to sound's first character.
- sound's last character is equal to delightful's first character.
- delightful's last character is equal to leetcode's first character.
The sentence is circular.

Example 2:
Input: sentence = "eetcode"
Output: true
Explanation: The words in sentence are ["eetcode"].
- eetcode's last character is equal to eetcode's first character.
The sentence is circular.

Example 3:
Input: sentence = "Leetcode is cool"
Output: false
Explanation: The words in sentence are ["Leetcode", "is", "cool"].
- Leetcode's last character is not equal to is's first character.
The sentence is not circular.

Constraints:
1 <= sentence.length <= 500
sentence consist of only lowercase and uppercase English letters and spaces.
The words in sentence are separated by a single space.
There are no leading or trailing spaces.

Hint 1
Check the character before the empty space and the character after the empty space.
Hint 2
Check the first character and the last character of the sentence.

Solution
✏️ Easy Python solution with splitting a sentence into words
Intuition
Split sentence to word for compact solution
"""

# Runtime 9 ms Beats 88.51%
# Memory 11.78 MB Beats 29.89%
def isCircularSentence(sentence):
    """
    :type sentence: str
    :rtype: bool
    """
    s=sentence.split(); ll=len(s)
    if ll==1:
        return sentence[0]==sentence[-1]
    else:
        s=[s[-1][-1]]+s+[s[0][0]]
        return all([s[i-1][-1]==s[i][0] for i in range(1,ll+1)])

# print(isCircularSentence("leetcode exercises sound delightful")) # True
# print(isCircularSentence("eetcode")) # True
# print(isCircularSentence("Leetcode is cool"))
print(isCircularSentence("Leetcode eisc cool"))