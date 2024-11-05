"""
05.11.2024. Topics: Shell
194. Transpose File
https://leetcode.com/problems/transpose-file/description/

Given a text file file.txt, transpose its content.
You may assume that each row has the same number of columns,
and each field is separated by the ' ' character.

Example:
If file.txt has the following content:
name age
alice 21
ryan 30

Output the following:
name alice ryan
age 21 30
"""

# https://leetcode.com/problems/transpose-file/solutions/2057914/is-using-python-fine/

# Read from the file file.txt and print its transposed content to stdout.
# python3 -c '
from collections import defaultdict
data = defaultdict(list)
with open("file_0194.txt") as f:
   for line in f:
       for i, word in enumerate(line.split()):
           data[i].append(word)
print(data)
for line in data.values():
    print(" ".join(line))