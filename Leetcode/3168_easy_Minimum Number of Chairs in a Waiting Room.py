"""
Done 23.06.2024. Topics: String,

3168. Minimum Number of Chairs in a Waiting Room
https://leetcode.com/problems/find-the-number-of-good-pairs-i/

You are given a string s. Simulate events at each second i:

If s[i] == 'E', a person enters the waiting room and takes one of the chairs in it.
If s[i] == 'L', a person leaves the waiting room, freeing up a chair.
Return the minimum number of chairs needed so that a chair is available
for every person who enters the waiting room given that it is initially empty.

Example 1:
Input: s = "EEEEEEE"
Output: 7
Explanation:
After each second, a person enters the waiting room and no person leaves it. Therefore, a minimum of 7 chairs is needed.

Example 2:
Input: s = "ELELEEL"
Output: 2
Explanation:
Let's consider that there are 2 chairs in the waiting room. The table below shows the state of the waiting room at each second.
Second	Event	People in the Waiting Room	Available Chairs
0	Enter	1	1
1	Leave	0	2
2	Enter	1	1
3	Leave	0	2
4	Enter	1	1
5	Enter	2	0
6	Leave	1	1

Example 3:
Input: s = "ELEELEELLL"
Output: 3
Explanation:
Let's consider that there are 3 chairs in the waiting room. The table below shows the state of the waiting room at each second.
Second	Event	People in the Waiting Room	Available Chairs
0	Enter	1	2
1	Leave	0	3
2	Enter	1	2
3	Enter	2	1
4	Leave	1	2
5	Enter	2	1
6	Enter	3	0
7	Leave	2	1
8	Leave	1	2
9	Leave	0	3

Hint 1
Iterate from left to right over the string and keep track of the number of people in the waiting room using a variable that you will increment on every occurrence of ‘E’ and decrement on every occurrence of ‘L’.
Hint 2
The answer is the maximum number of people in the waiting room at any instance.
"""

# Runtime 16 ms Beats 60.42%
# Memory 11.45 MB Beats 94.23%
# Runtime 8 ms Beats 96.56%
# Memory 11.66 MB Beats 31.82%

def minimumChairs(s):
    """
    :type s: str
    :rtype: int
    """

    mmax=0;    curr=0
    for s1 in s:
        if s1=="E":
            curr=curr+1
            mmax=max(mmax,curr)
        else:
            curr=curr-1
    return mmax


