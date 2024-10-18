"""
Done 18.10.2024. Topics: Array, String, Simulation
68. Text Justification
https://leetcode.com/problems/text-justification/description/

Given an array of strings words and a width maxWidth, format the text such that each line has exactly
maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line.
Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible.
If the number of spaces on a line does not divide evenly between words,
the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:
A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.

Example 1:
Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Example 2:
Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be",
because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.

Example 3:
Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.",
"Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]

Constraints:
1 <= words.length <= 300
1 <= words[i].length <= 20
words[i] consists of only English letters and symbols.
1 <= maxWidth <= 100
words[i].length <= maxWidth

My Solution
✏️ Easy and very fast (1 ms) , but long Python solution for Problem 0068 (Text Justification)
https://leetcode.com/problems/text-justification/solutions/5931411/easy-and-very-fast-1-ms-but-long-python-solution-for-problem-0068-text-justification/

Intuition
Two stage of solution
- distribute words by string
- correct justification strings
Approach
Done 18.10.2024.
Why is this task of the type "hard"? and Acceptance 45.5%?
Not every "easy" level task is that simple.
"""

# Runtime 1 ms Beats 99.85%
# Memory 11.81 MB Beats 9.68%
# Time Complexity O(N)
# Space Complexity O(N)

def fullJustify(words, maxWidth):
    """
    :type words: List[str]
    :type maxWidth: int
    :rtype: List[str]
    """
    ll=len(words)
    lll=[len(words[i]) for i in range(ll)]
    i=0; res=[]
    # part-1 distribute words by string
    while i<ll:
        tmp=''; lln=0
        for j in range(i,ll):
            if lln + lll[j]<=maxWidth:
                lln += lll[j]
                tmp = tmp + words[j]
                i+=1
            else: break
            if lln + 1<= maxWidth:
                lln+=1
                tmp = tmp + ' '
            else: break
        res.append(tmp)
    # part-2 justification strings
    print(res)
    llr=len(res)
    for i in range(llr):
        s=res[i].strip()
        nw=s.split(); lnw=len(nw); lnw1=lnw-1
        if i==llr-1 or lnw==1:
            res[i]=s.ljust(maxWidth,' ')
        else:
            num_sp=maxWidth-sum([len(s) for s in nw])
            main_sp=num_sp//lnw1
            rest_sp=num_sp%lnw1
            s=''
            for j in range(lnw):
                if j != lnw-1:
                    s=s + nw[j] + ' '*main_sp
                    if j != lnw-2 and rest_sp >0:
                        s+=' '
                        rest_sp-=1
                else:
                    s = s + nw[j]
            res[i]=s
    return res

from pprint import pp
from icecream import ic
# print(fullJustify(words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16))
# print(fullJustify(words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16))
# pp(fullJustify(words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20))
pp(fullJustify(words = ["ask","not","what","your","country","can","do","for","you","ask","what","you","can","do","for","your","country"], maxWidth = 16))
