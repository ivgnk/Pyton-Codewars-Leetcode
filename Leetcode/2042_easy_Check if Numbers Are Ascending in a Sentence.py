'''
2042. Check if Numbers Are Ascending in a Sentence
https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/

A sentence is a list of tokens separated by a single space with no leading or trailing spaces.
Every token is either a positive number consisting of digits 0-9 with no leading zeros,
or a word consisting of lowercase English letters.

For example, "a puppy has 2 eyes 4 legs" is a sentence with seven tokens:
"2" and "4" are numbers and the other tokens such as "puppy" are words.
Given a string s representing a sentence, you need to check
if all the numbers in s are strictly increasing from left to right
(i.e., other than the last number, each number is strictly smaller than the number on its right in s).
Return true if so, or false otherwise.

Example 1:
example-1
Input: s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles"
Output: true
Explanation: The numbers in s are: 1, 3, 4, 6, 12.
They are strictly increasing from left to right: 1 < 3 < 4 < 6 < 12.

Example 2:
Input: s = "hello world 5 x 5"
Output: false
Explanation: The numbers in s are: 5, 5. They are not strictly increasing.
Example 3:

example-3
Input: s = "sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"
Output: false
Explanation: The numbers in s are: 7, 51, 50, 60. They are not strictly increasing.
'''

# Runtime 10 ms Beats 84.17% of users with Python
# Memory 11.70 MB Beats 76.67% of users with Python

def areNumbersAscending(s):
    """
    :type s: str
    :rtype: bool
    """
    s1=s.split()
    res=[int(s2) for s2 in s1 if s2.isdigit()]
    res1=sorted(res)
    if res==res1:
        return len(res)==len(set(res))
    return False

print(areNumbersAscending('1 box has 3 blue 4 red 6 green and 12 yellow marbles'))
