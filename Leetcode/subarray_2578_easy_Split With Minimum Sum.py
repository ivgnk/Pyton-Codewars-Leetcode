"""
Done 30.06.2024. Topics: Math, Sorting
2578. Split With Minimum Sum
https://leetcode.com/problems/split-with-minimum-sum/description/

Given a positive integer num, split it into two non-negative integers num1 and num2 such that:

The concatenation of num1 and num2 is a permutation of num.
In other words, the sum of the number of occurrences of each digit in num1 and num2
is equal to the number of occurrences of that digit in num.
num1 and num2 can contain leading zeros.
Return the minimum possible sum of num1 and num2.

Notes:
It is guaranteed that num does not contain any leading zeros.
The order of occurrence of the digits in num1 and num2 may differ from the order of occurrence of num.


Example 1:

Input: num = 4325
Output: 59
Explanation: We can split 4325 so that num1 is 24 and num2 is 35, giving a sum of 59.
We can prove that 59 is indeed the minimal possible sum.
Example 2:

Input: num = 687
Output: 75
Explanation: We can split 687 so that num1 is 68 and num2 is 7,
which would give an optimal sum of 75.

Constraints:
10 <= num <= 109

as hint https://leetcode.com/problems/split-with-minimum-sum/description/comments/2389555
Approach->
1/ String Conversion: Convert the integer num to a string s using to_string(num).
This operation takes O(log num) time.

2. String Sorting: Sort the characters in the string s using sort(s.begin(), s.end()).
Sorting the string takes O(d log d) time, where d is the number of digits in the integer num.

3/ Digit Extraction and Integer Formation: Iterate through the sorted string s and form two integers, num1 and num2,
by combining every two consecutive digits. This step takes O(d) time.
"""

# Runtime 15 ms Beats 47.19%
# Memory 11.52 MB Beats 64.04%
# Runtime 6 ms Beats 98.88%
# Memory 11.40 MB Beats 98.88%
# https://leetcode.com/problems/split-with-minimum-sum/submissions/1304995530/
def splitNum(num):
    """
    :type num: int
    :rtype: int
    """
    s=sorted(str(num))
    s1,s2 = '', ''
    for i in range(len(s)):
        if i%2==0:
            s1 = s1 + s[i]
        else:
            s2 = s2 + s[i]
    return int(s1)+int(s2)

print(splitNum(4325))
print(splitNum(687))