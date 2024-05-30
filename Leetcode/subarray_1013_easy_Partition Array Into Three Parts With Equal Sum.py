"""
30.05.2024. Topics: Array, Greedy

1013. Partition Array Into Three Parts With Equal Sum
https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/description/

Given an array of integers arr, return true if we can partition the array into three non-empty parts with equal sums.
Formally, we can partition the array if we can find indexes i + 1 < j with (arr[0] + arr[1] + ... + arr[i] ==
arr[i + 1] + arr[i + 2] + ... + arr[j - 1] == arr[j] + arr[j + 1] + ... + arr[arr.length - 1])

Example 1:
Input: arr = [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1

Example 2:
Input: arr = [0,2,1,-6,6,7,9,-1,2,0,1]
Output: false

Example 3:
Input: arr = [3,3,6,5,-2,2,5,1,-9,4]
Output: true
Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4

Companies
Hint 1
If we have three parts with the same sum, what is the sum of each?
If you can find the first part, can you find the second part?
"""

from collections import Counter

# Wrong Answer -- 71 / 72 testcases passed
def canThreePartsEqualSum2(arr):
    """
    :type arr: List[int]
    :rtype: bool
    """
    ll = len(arr)
    ssum = sum(arr)
    if ssum % 3 != 0: return False
    if max(arr) == min(arr) == 0: return True

    c = Counter(arr)
    ind = list(c);    dd = dict(c)
    if len(ind) == 2 and ind[0] == -ind[1] and dd[ind[0]] == dd[ind[1]]:
        return dd[ind[0]] >= 3

    spart = ssum // 3
    s1 = 0;    npart = 0
    for i in range(ll):
        s1 = s1 + arr[i]
        if s1 == spart:
            npart = npart + 1
            s1 = 0
    return npart == 3  # or (npart == 2 and s1==spart)

print(canThreePartsEqualSum2([10,-10,10,-10,10,-10,10,-10]))


# Runtime 220 ms Beats 90.91% of users with Python
# Memory 17.50 MB Beats 68.83% of users with Python

# https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/solutions/2569040/80-faster-easy-and-optimal-solution/
def canThreePartsEqualSum4(arr):
    res = sum(arr)
    if (res % 3 != 0):
        return False
    res = res // 3
    li = 0
    sm = 0
    for i in arr:
        sm += i
        if (sm == res):
            li += 1
            sm = 0
        if (li == 3):
            return True
    return li == 3


# Runtime 229 ms Beats 66.23% of users with Python
# Memory 17.50 MB Beats 44.16% of users with Python
# https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/solutions/3489641/beats-100-java-c-python-o-n-solution-explained/
def canThreePartsEqualSum5(arr):
    total_sum = sum(arr)
    if total_sum % 3 != 0:
        return False

    target = total_sum // 3
    current_sum = 0
    count = 0

    for i in range(len(arr) - 1):
        current_sum += arr[i]
        if current_sum == target:
            current_sum = 0
            count += 1
            if count == 2:
                return True

    return False

