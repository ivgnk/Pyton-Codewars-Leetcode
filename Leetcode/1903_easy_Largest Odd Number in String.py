"""
Done 28.08.2024. Topics: Math, String, Greedy

1903. Largest Odd Number in String
https://leetcode.com/problems/largest-odd-number-in-string/description/

You are given a string num, representing a large integer.
Return the largest-valued odd integer (as a string) that is a non-empty substring of num,
or an empty string "" if no odd integer exists.
A substring is a contiguous sequence of characters within a string.

Example 1:
Input: num = "52"
Output: "5"
Explanation: The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.

Example 2:
Input: num = "4206"
Output: ""
Explanation: There are no odd numbers in "4206".

Example 3:
Input: num = "35427"
Output: "35427"
Explanation: "35427" is already an odd number.

Constraints:
1 <= num.length <= 105
num only consists of digits and does not contain any leading zeros.

Hint 1
In what order should you iterate through the digits?
Hint 2
If an odd number exists, where must the number start from?

Solution
✏️ Easy Python solution with searching in a string from the end
Intuition
The desired number must end in an odd digit.

Approach
We look from the end of the line: if we find an odd number,
then we take the line from the beginning to this number

Done 28.08.2024
Runtime 45 ms Beats 83.57%
Memory 16.85 MB Beats 65.22%

"""

# Смотрим с конца:
# если находим нечетное число, то берем строку от начала до этого числа

# Runtime 45 ms Beats 83.57%
# Memory 16.85 MB Beats 65.22%

odd_str = ["1", "3", "5", "7", "9"]
def largestOddNumber(num):
    """
    :type num: str
    :rtype: str
    """
    ll=len(num)
    for i in range(ll-1,-1,-1):
        if num[i] in odd_str:
            return num[:i+1]
    return ""

print(largestOddNumber("52"))
print(largestOddNumber("4206"))
print(largestOddNumber("35427"))