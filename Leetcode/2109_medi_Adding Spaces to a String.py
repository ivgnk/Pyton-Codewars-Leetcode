"""
Done 03.12.2024. Topics: Array, String
2109. Adding Spaces to a String
https://leetcode.com/problems/adding-spaces-to-a-string/description/

You are given a 0-indexed string s and a 0-indexed integer array spaces that
describes the indices in the original string where spaces will be added.
Each space should be inserted before the character at the given index.

For example, given s = "EnjoyYourCoffee" and spaces = [5, 9],
we place spaces before 'Y' and 'C', which are at indices 5 and 9 respectively.
Thus, we obtain "Enjoy Your Coffee".
Return the modified string after the spaces have been added.

Example 1:
Input: s = "LeetcodeHelpsMeLearn", spaces = [8,13,15]
Output: "Leetcode Helps Me Learn"
Explanation:
The indices 8, 13, and 15 correspond to the underlined characters in "LeetcodeHelpsMeLearn".
We then place spaces before those characters.

Example 2:
Input: s = "icodeinpython", spaces = [1,5,7,9]
Output: "i code in py thon"
Explanation:
The indices 1, 5, 7, and 9 correspond to the underlined characters in "icodeinpython".
We then place spaces before those characters.

Example 3:
Input: s = "spacing", spaces = [0,1,2,3,4,5,6]
Output: " s p a c i n g"
Explanation:
We are also able to place spaces before the first character of the string.

Constraints:
1 <= s.length <= 3 * 105
s consists only of lowercase and uppercase English letters.
1 <= spaces.length <= 3 * 105
0 <= spaces[i] <= s.length - 1
All the values of spaces are strictly increasing.

Hint 1
Create a new string, initially empty, as the modified string. Iterate through the original string and append each character of the original string to the new string. However, each time you reach a character that requires a space before it, append a space before appending the character.
Hint 2
Since the array of indices for the space locations is sorted, use a pointer to keep track of the next index to place a space. Only increment the pointer once a space has been appended.
Hint 3
Ensure that your append operation can be done in O(1).

Runtime 183 ms Beats 38.46%
Memory 60.00 MB Beats 5.72%
Time Complexity O(N)
Space Complexity O(N)

My solution ✏️ Easy Python solution for Problem 2109
https://leetcode.com/problems/adding-spaces-to-a-string/solutions/6108535/easy-python-solution-for-problem-2109/
"""

def addSpaces(s, spaces):
    """
    :type s: str
    :type spaces: List[int]
    :rtype: str
    """
    lst=[]; n=0; nmax=len(spaces)
    for i in range(len(s)):
        if n==nmax: lst.append(s[i])
        else:
            if i!=spaces[n]:
                lst.append(s[i])
            else:
                lst.append(' '+s[i])
                n+=1
    return ''.join(lst)

class Solution:
    def addSpaces(self, s, spaces):
        arr = []
        prev = 0
        for space in spaces:
            arr.append(s[prev:space])
            prev = space
        arr.append(s[space:])
        return " ".join(arr)

print(addSpaces(s = "LeetcodeHelpsMeLearn", spaces = [8,13,15]))
print(addSpaces(s = "icodeinpython", spaces = [1,5,7,9]))
print(addSpaces(s = "spacing", spaces = [0,1,2,3,4,5,6]))