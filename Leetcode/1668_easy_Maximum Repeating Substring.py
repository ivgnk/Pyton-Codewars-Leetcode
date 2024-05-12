"""
Done 12.05.2024. Topics: String
1668. Maximum Repeating Substring
https://leetcode.com/problems/maximum-repeating-substring/description/

For a string sequence, a string word is k-repeating if word concatenated k times is a substring of sequence.
The word's maximum k-repeating value is the highest value k where word is k-repeating in sequence.
If word is not a substring of sequence, word's maximum k-repeating value is 0.
Given strings sequence and word, return the maximum k-repeating value of word in sequence.

Example 1:
Input: sequence = "ababc", word = "ab"
Output: 2
Explanation: "abab" is a substring in "ababc".

Example 2:
Input: sequence = "ababc", word = "ba"
Output: 1
Explanation: "ba" is a substring in "ababc". "baba" is not a substring in "ababc".

Example 3:
Input: sequence = "ababc", word = "ac"
Output: 0
Explanation: "ac" is not a substring in "ababc".

Hint 1
The constraints are low enough for a brute force approach.
Hint 2
Try every k value from 0 upwards until word is no longer k-repeating.
"""

# Runtime 10 ms Beats 81.82% of users with Python
# Memory 11.69 MB Beats 62.73% of users with Python

def maxRepeating(sequence, word):
    """
    :type sequence: str
    :type word: str
    :rtype: int
    """
    n=sequence.find(word)
    if n==-1:
        return 0
    else:
        n = sequence.find(word)
        if n == -1:
            return 0
        else:
            ll = len(sequence); lw = len(word)
            if sequence == word: return 1
            z = ll // lw; wz = word * z
            if ll % lw == 0:
                if sequence == wz: return z
            else:
                if sequence[:lw * z] == wz: return z

            for i in range(5, 0, -1):
                if sequence[:lw * i] == word * i:
                    if sequence[lw * i:].find(word) == -1:
                        return i
                    elif sequence[lw * i:].find(word * (i + 1)) == -1:
                        return i

            for i in range(8, 0, -1):
                if word * i in sequence:  return i

            # nn= [i for i in range(ll-lw+1) if sequence[i:i+lw]==word]
            # if len(nn)==1: return 1
            # nnn=1; res=[]
            # for i in range(1,len(nn)):
            #     if nn[i]==nn[i-1]+lw:
            #         nnn=nnn+1
            #     else:
            #         res.append(nnn)
            #         nnn=1
            # res.append(nnn)
            # return max(res)


print(maxRepeating(sequence = "aaaaabababaabbababbbbaaaaabbbabaabaaabaabbbaabbbaabaabababbbba", word = "aa"))
