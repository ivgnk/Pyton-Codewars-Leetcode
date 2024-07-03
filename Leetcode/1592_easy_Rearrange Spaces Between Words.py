"""
Done 03.07.2024. Topics: String
1592. Rearrange Spaces Between Words
https://leetcode.com/problems/rearrange-spaces-between-words/description/

You are given a string text of words that are placed among some number of spaces.
Each word consists of one or more lowercase English letters and are separated by at least one space.
It's guaranteed that text contains at least one word.
Rearrange the spaces so that there is an equal number of spaces between every pair of
adjacent words and that number is maximized.

If you cannot redistribute all the spaces equally, place the extra spaces at the end,
meaning the returned string should be the same length as text.
Return the string after rearranging the spaces.



Example 1:
Input: text = "  this   is  a sentence "
Output: "this   is   a   sentence"
Explanation: There are a total of 9 spaces and 4 words. We can evenly divide the 9 spaces between the words: 9 / (4-1) = 3 spaces.

Example 2:
Input: text = " practice   makes   perfect"
Output: "practice   makes   perfect "
Explanation: There are a total of 7 spaces and 3 words. 7 / (3-1) = 3 spaces plus 1 extra space. We place this extra space at the end of the string.

Constraints:

1 <= text.length <= 100
text consists of lowercase English letters and ' '.
text contains at least one word.

Hint 1
Count the total number of spaces and words.
Then use the integer division to determine the numbers of spaces
to add between each word and at the end.
"""

# Runtime 14 ms Beats 53.13%
# Memory 11.50 MB Beats 100.00%
# Runtime 8 ms Beats 95.31%
# Memory 11.48 MB Beats 100.00%

from icecream import ic
def reorderSpaces(text):
    """
    :type text: str
    :rtype: str
    """
    nsp=text.count(' ')
    t1=text.strip().split()
    nw=len(t1)
    if nw==1:
        return t1[0] + ' ' * nsp
    else:
        s=''
        l1=nsp//(nw-1); l2=nsp-l1*(nw-1)
        for i,w in enumerate(t1):
            if i<nw-1:
                s=s+w+' '*l1
            else:
                s= s+w+' '*l2
        return s
print(reorderSpaces("  this   is  a sentence "))