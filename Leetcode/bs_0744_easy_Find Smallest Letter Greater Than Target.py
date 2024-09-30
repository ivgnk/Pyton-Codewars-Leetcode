"""
Done 30.09.2024. Topics: Array, Binary Search
744. Find Smallest Letter Greater Than Target
https://leetcode.com/problems/find-smallest-letter-greater-than-target/description

You are given an array of characters letters that is sorted in non-decreasing order, and a character target.
There are at least two different characters in letters.
Return the smallest character in letters that is lexicographically greater than target.
If such a character does not exist, return the first character in letters.

Example 1:
Input: letters = ["c","f","j"], target = "a"
Output: "c"
Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.

Example 2:
Input: letters = ["c","f","j"], target = "c"
Output: "f"
Explanation: The smallest character that is lexicographically greater than 'c' in letters is 'f'.

Example 3:
Input: letters = ["x","x","y","y"], target = "z"
Output: "x"
Explanation: There are no characters in letters that is lexicographically greater than 'z' so we return letters[0].

Constraints:
2 <= letters.length <= 10**4
letters[i] is a lowercase English letter.
letters is sorted in non-decreasing order.
letters contains at least two different characters.
target is a lowercase English letter.

Hint 1
Try to find whether each of 26 next letters are in the given string array.

in discussion
My linear search takes less time than my binary search
https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/comments/1922039
big O is only eventually true for large enough N.
I guess for small N in an easy problem(2 <= letters.length <= 10^4),
overheads for simple loop are easier to optimize than some branching logics binary search uses.
https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/comments/1922043
If you are thinking of using Binary Search, then SUGGESTION: Don't use!!!
https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/comments/2496818

Solution
✏️ Easiest (but fast) Python solution without binary search
# Intuition
The simplest approach is always needed first
"""

# Runtime 65 ms Beats 85.40%
# Memory 13.68 MB Beats 24.26%
# Time Complexity O(N)
# Space Complexity O(1)
def nextGreatestLetter(letters, target):
    """
    :type letters: List[str]
    :type target: str
    :rtype: str
    """
    ll = len(letters)
    for i, s in enumerate(letters):
        if s > target:
            if i == ll or i==0:
                return letters[0]
            else:
                return letters[i]
    else: return letters[0]

print(nextGreatestLetter(letters = ["c","f","j"], target = "a"))
print(nextGreatestLetter(letters = ["c","f","j"], target = "c"))
