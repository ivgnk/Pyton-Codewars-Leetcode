"""
Done 07.05.2024. Topics: Array, Hash Table, String
804. Unique Morse Code Words
https://leetcode.com/problems/unique-morse-code-words/description/

International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows:

'a' maps to ".-",
'b' maps to "-...",
'c' maps to "-.-.", and so on.
For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
Given an array of strings words where each word can be written as a concatenation of the Morse code of each letter.

For example, "cab" can be written as "-.-..--...", which is the concatenation of "-.-.", ".-", and "-...". We will call such a concatenation the transformation of a word.
Return the number of different transformations among all words we have.

Example 1:
Input: words = ["gin","zen","gig","msg"]
Output: 2
Explanation: The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."
There are 2 different transformations: "--...-." and "--...--.".

Example 2:
Input: words = ["a"]
Output: 1
"""

# Runtime 18 ms Beats 56.14% of users with Python
# Memory 11.66 MB Beats 73.39% of users with Python
# Runtime 9 ms Beats 96.78% of users with Python
# Memory 11.92 MB Beats 11.40% of users with Python

basem = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
basee = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def uniqueMorseRepresentations(words):
    """
    :type words: List[str]
    :rtype: int
    """
    if len(words)==1:return 1
    dd=dict(zip(basee,basem))
    rlst =[(''.join(dd[s] for s in w)) for w in words ]
    return len(set(rlst))

print(uniqueMorseRepresentations(["gin","zen","gig","msg"]))