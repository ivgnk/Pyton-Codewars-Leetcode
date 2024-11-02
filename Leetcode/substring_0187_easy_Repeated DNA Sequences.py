"""
Done 03.11.2024. Topics: Hash Table
187. Repeated DNA Sequences
https://leetcode.com/problems/repeated-dna-sequences

The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings)
that occur more than once in a DNA molecule. You may return the answer in any order.

Example 1:
Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]

Example 2:
Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]

Constraints:
1 <= s.length <= 105
s[i] is either 'A', 'C', 'G', or 'T'.
"""
# Runtime 57 ms Beats 15.11%
# Memory 38.56 MB Beats 8.38%

from collections import defaultdict
def findRepeatedDnaSequences(s):
    """
    :type s: str
    :rtype: List[str]
    """
    dd=defaultdict(int)
    for i in range(len(s)-10):
        dd[s[i:i+10]]+=1
    return [k for k,v in dd.items() if v>1]

print(findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))