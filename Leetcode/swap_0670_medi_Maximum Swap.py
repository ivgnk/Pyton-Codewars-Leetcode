"""
Done 17.10.2024. Topics: Math, Greedy,
670. Maximum Swap
https://leetcode.com/problems/maximum-swap/description/

You are given an integer num.
You can swap two digits at most once to get the maximum valued number.
Return the maximum valued number you can get.

Example 1:
Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.

Example 2:
Input: num = 9973
Output: 9973
Explanation: No swap.

Constraints:
0 <= num <= 10**8

tip in discussion
Convert the digit to a string - iterate a variable 'i' from 0 to numString.Length.
This 'i' variable will point to the current digit that we're considering swapping for something larger.
Then iterate a variable 'j' from numString.Length - 1 to i, and ask two things:
A. Is the character located at index j greater in value than the character located at index i?
B. Is the character located at index j greater in value than the current largest character
we've found to replace the char at index i?

If both are true, we can save the index of that max character,
and have some boolean that will indicate that we've found a valid swap for char at index 'i'.
https://leetcode.com/problems/maximum-swap/description/comments/2174155
from https://leetcode.com/u/Cocamo1337/

My solution
https://leetcode.com/problems/maximum-swap/solutions/5925027/python-solution-for-problem-0670-based-on-tip-in-discussion/
"""

# Time Complexity O(N**2)
# Space Complexity O(N)
# Runtime 11 ms Beats 76.04%
# Memory 11.54 MB Beats 61.67%

from collections import Counter
def maximumSwap(num):
    """
    :type num: int
    :rtype: int
    """
    s = str(num); ll=len(s)
    lst=list(s)
    fnd=''
    for i in range(ll):
        for j in range(ll-1,i,-1):
            if s[j]>s[i]:
                if s[j]>fnd:
                    fnd=s[j]
                    i1=i
                    j1=j
    if fnd !='':
        lst[i1], lst[j1] = lst[j1], lst[i1]
        return int(''.join(lst))
    else:
        return num


print(maximumSwap(2736))
print(maximumSwap(9973))