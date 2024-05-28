"""
Done 29.05.2024. Topics: String, Stack
2390. Removing Stars From a String
https://leetcode.com/problems/removing-stars-from-a-string/description/

You are given a string s, which contains stars *.
In one operation, you can:
Choose a star in s.
Remove the closest non-star character to its left, as well as remove the star itself.
Return the string after all stars have been removed.
Note:
The input will be generated such that the operation is always possible.
It can be shown that the resulting string will always be unique.

Example 1:
Input: s = "leet**cod*e"
Output: "lecoe"
Explanation: Performing the removals from left to right:
- The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
- The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
- The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
There are no more stars, so we return "lecoe".
Example 2:

Input: s = "erase*****"
Output: ""
Explanation: The entire string is removed, so we return an empty string.

Hint 1
What data structure could we use to efficiently perform these removals?
Hint 2
Use a stack to store the characters. Pop one character off the stack at each star. Otherwise, we push the character onto the stack.
"""

# https://leetcode.com/problems/removing-stars-from-a-string/solutions/2576123/python-98-faster-easy-solution/
# Runtime 278 ms Beats 65.63% of users with Python
# Memory 15.09 MB Beats 23.73% of users with Python
def removeStars(self, s):
    """
    :type s: str
    :rtype: str
    """
    s_list = list(s)
    output = []
    for letter in s_list:
        if letter != "*":
            output.append(letter)
        else:
            output.pop()
    return "".join(output)

# Runtime 9214 ms Beats 5.01% of users with Python
# Memory 14.30 MB Beats 80.35% of users with Python

def removeStars(self, s):
    """
    :type s: str
    :rtype: str
    """
    lst = []
    for i in s:
        if i != '*':
            lst.insert(0, i)
        else:
            lst.pop(0)
    lst.reverse()
    return ''.join(lst)


# Runtime 9350 ms Beats 5.01% of users with Python
# Memory 16.94 MB Beats 14.51% of users with Python
def removeStars(s):
    lst=[]
    for i in range(len(s)):
        if s[i] !='*':
            lst.insert(0,s[i])
        else:
            lst.pop(0)
    lst.reverse()
    return ''.join(lst)

def removeStars2(s):
    ll=len(s)
    lst=[]
    for i in range(ll):
        if s[i] !='*':
            lst.insert(0,s[i])
        else:
            lst.pop(0)
    lst.reverse()
    return ''.join(lst)

print(removeStars("leet**cod*e"))



