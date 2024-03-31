'''
1309. Decrypt String from Alphabet to Integer Mapping
https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/description/

You are given a string s formed by digits and '#'. We want to map s to English lowercase characters as follows:
Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
Return the string formed after mapping.

The test cases are generated so that a unique mapping will always exist.

Example 1:
Input: s = "10#11#12"
Output: "jkab"
Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".

Example 2:
Input: s = "1326#"
Output: "acz"
'''

# Runtime 12 ms Beats 81.15% of users with Python
# Memory 11.73 MB Beats 41.80% of users with Python

# abcdefghijklmnopqrstuvwxyz
def freqAlphabets(s):
    """
    :type s: str
    :rtype: str
    """
    l='abcdefghijklmnopqrstuvwxyz'
    for i in range(10,27):
        s1=str(i)+'#'
        if s1 in s:
            s=s.replace(s1,l[i-1])
        if '#' not in s1: break
    for i in range(1,10):
        s1=str(i)
        if s1 in s:
            s = s.replace(s1, l[i-1])
    return s

print(freqAlphabets('10#11#12'))
print(freqAlphabets("acz"))
print(freqAlphabets("12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"))