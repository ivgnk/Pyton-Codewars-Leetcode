"""
Done 22.06.2024. Topics: Sorting
2231. Largest Number After Digit Swaps by Parity
https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/

You are given a positive integer num. You may swap any two digits of num that have the same parity
(i.e. both odd digits or both even digits).
Return the largest possible value of num after any number of swaps.

Example 1:
Input: num = 1234
Output: 3412
Explanation: Swap the digit 3 with the digit 1, this results in the number 3214.
Swap the digit 2 with the digit 4, this results in the number 3412.
Note that there may be other sequences of swaps but it can be shown that 3412 is the largest possible number.
Also note that we may not swap the digit 4 with the digit 1 since they are of different parities.

Example 2:
Input: num = 65875
Output: 87655
Explanation: Swap the digit 8 with the digit 6, this results in the number 85675.
Swap the first digit 5 with the digit 7, this results in the number 87655.
Note that there may be other sequences of swaps but it can be shown that 87655 is the largest possible number.

Hint 1
The bigger digit should appear first (more to the left) because it contributes more to the value of the number.
Hint 2
Get all the even digits, as well as odd digits. Sort them separately.
Hint 3
Reconstruct the number by giving the earlier digits the highest available digit of the same parity.
"""

# Runtime 21 ms Beats 26.41%
# Memory 11.44 MB Beats 88.68%
# Runtime 11 ms Beats 84.91%
# Memory 11.48 MB Beats 88.68%

def largestInteger(num):
    """
    :type num: int
    :rtype: int
    """
    eve_=[]; odd_=[]
    s=str(num)
    ll= len(s); rll=range(ll)
    ev_ind=[]
    for i in rll:
        ii=int(s[i])
        if ii % 2 == 0:
            eve_.append(s[i])
            ev_ind.append(True)
        else:
            odd_.append(s[i])
            ev_ind.append(False)

    eve_.sort(reverse=True)
    odd_.sort(reverse=True)
    ress=''; ne=0; no=0
    for i in rll:
        if ev_ind[i]:
            ress=ress+eve_[ne]
            ne=ne+1
        else:
            ress=ress+odd_[no]
            no=no+1
    return int(ress)


