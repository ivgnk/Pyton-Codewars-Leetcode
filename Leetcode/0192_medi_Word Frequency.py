"""
05.11.2024. Topics: Shell
192. Word Frequency
https://leetcode.com/problems/word-frequency/description/

Write a bash script to calculate the frequency of each word in a text file words.txt.
For simplicity sake, you may assume:
- words.txt contains only lowercase characters and space ' ' characters.
- Each word must consist of lowercase characters only.
- Words are separated by one or more whitespace characters.

Example:
Assume that words.txt has the following content:
the day is sunny the the
the sunny is is

Your script should output the following, sorted by descending frequency:

the 4
is 3
sunny 2
day 1

Note:
Don't worry about handling ties, it is guaranteed that each word's frequency count is unique.
Could you write it in one-line using Unix pipes?
"""

# Runtime 141 ms Beats 5.24%
# Memory 8.96 MB Beats 18.26%

# python3 -c '
from collections import defaultdict
data = defaultdict(int)
with open("words.txt") as f:
   for line in f:
       for word in line.split():
           data[word]+=1
lst=sorted([(v,k) for k,v in data.items()], reverse=True)
for n,w in lst:
    print(w, n)