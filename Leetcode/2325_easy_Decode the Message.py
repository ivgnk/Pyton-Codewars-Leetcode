"""
2325. Decode the Message
https://leetcode.com/problems/decode-the-message/description/

ou are given the strings key and message, which represent a cipher key and a secret message, respectively. The steps to decode message are as follows:

1) Use the first appearance of all 26 lowercase English letters in key as the order of the substitution table.
2) Align the substitution table with the regular English alphabet.
3) Each letter in message is then substituted using the table.
4) Spaces ' ' are transformed to themselves.

For example, given key = "happy boy" (actual key would have at least one instance of each letter in the alphabet),
we have the partial substitution table of ('h' -> 'a', 'a' -> 'b', 'p' -> 'c', 'y' -> 'd', 'b' -> 'e', 'o' -> 'f').
Return the decoded message.

Example 1:
Input: key = "the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv"
Output: "this is a secret"
Explanation: The diagram above shows the substitution table.
It is obtained by taking the first appearance of each letter in "the quick brown fox jumps over the lazy dog"
"""

# Runtime 16 ms Beats 75.71% of users with Python
# Memory 11.96 MB Beats 6.29% of users with Python

def decodeMessage(key, message):
    """
    :type key: str
    :type message: str
    :rtype: str
    """
    alc='abcdefghijklmnopqrstuvwxyz'
    key=list(key.replace(" ",''))
    key2 = []
    # stackoverflow.com/questions/59782956/ways-to-save-sequence-of-elements-in-python-set
    for each in key:
        if each not in key2:
            key2.append(each)
    # print(key2)
    message2=list(message)
    # print(message,message2)
    res=[]
    for s in message2:
        if s==" ": res.append(s)
        else: res.append(alc[key2.index(s)])
    return ''.join(res)

print(decodeMessage(key = "the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv"))

