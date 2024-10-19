"""
Done 19.10.2024. Topics: Math, String, Sliding Window
2269. Find the K-Beauty of a Number
https://leetcode.com/problems/find-the-k-beauty-of-a-number/

The k-beauty of an integer num is defined as the number of substrings of num when
it is read as a string that meet the following conditions:
It has a length of k.
It is a divisor of num.
Given integers num and k, return the k-beauty of num.

Note:
Leading zeros are allowed.
0 is not a divisor of any value.
A substring is a contiguous sequence of characters in a string.

Example 1:
Input: num = 240, k = 2
Output: 2
Explanation: The following are the substrings of num of length k:
- "24" from "240": 24 is a divisor of 240.
- "40" from "240": 40 is a divisor of 240.
Therefore, the k-beauty is 2.

Example 2:
Input: num = 430043, k = 2
Output: 2
Explanation: The following are the substrings of num of length k:
- "43" from "430043": 43 is a divisor of 430043.
- "30" from "430043": 30 is not a divisor of 430043.
- "00" from "430043": 0 is not a divisor of 430043.
- "04" from "430043": 4 is not a divisor of 430043.
- "43" from "430043": 43 is a divisor of 430043.
Therefore, the k-beauty is 2.

Constraints:
1 <= num <= 109
1 <= k <= num.length (taking num as a string)

Hint 1
We should check all the substrings of num with a length of k and see if it is a divisor of num.
Hint 2
We can more easily obtain the substrings by converting num into a string and
converting back to an integer to check for divisibility.
"""

# Runtime 0 ms Beats 100.00%
# Memory 11.74 MB Beats 7.91%
def divisorSubstrings(num, k):
    """
    :type num: int
    :type k: int
    :rtype: int
    """
    s=str(num); n=0
    for i in range(len(s)-k+1):
        dat=int(s[i:i+k])
        print(i,s[i:i+k],dat)
        if dat !=0 and num%dat==0:
            n+=1
    return n

print(divisorSubstrings(240,2))