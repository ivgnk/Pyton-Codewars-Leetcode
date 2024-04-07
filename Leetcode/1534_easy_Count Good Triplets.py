'''
1534. Count Good Triplets
https://leetcode.com/problems/count-good-triplets/description/

Given an array of integers arr, and three integers a, b and c.
You need to find the number of good triplets.
A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:
0 <= i < j < k < arr.length
|arr[i] - arr[j]| <= a
|arr[j] - arr[k]| <= b
|arr[i] - arr[k]| <= c

Where |x| denotes the absolute value of x.
Return the number of good triplets.


Example 1:
Input: arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
Output: 4
Explanation: There are 4 good triplets: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)].

Example 2:
Input: arr = [1,1,2,2,3], a = 0, b = 0, c = 1
Output: 0
Explanation: No triplet satisfies all conditions.
'''

# Runtime 273 ms Beats 65.42% of users with Python3
# Memory 16.57 MB Beats 76.05%# of users with Python3

def countGoodTriplets(arr, a, b, c):
    n = 0;  ll = len(arr)
    for i in range(ll):
        for j in range(i+1, ll):
            for k in range(j+1, ll):
                if abs(arr[i] - arr[j]) <= a:
                    if abs(arr[j] - arr[k]) <= b:
                        if abs(arr[i] - arr[k]) <= c:
                            n += 1
    return n

print(countGoodTriplets(arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3))
print(countGoodTriplets(arr = [1,1,2,2,3], a = 0, b = 0, c = 1))