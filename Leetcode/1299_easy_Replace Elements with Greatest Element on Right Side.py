'''
Done 02.06. Topics: Array
1299. Replace Elements with Greatest Element on Right Side
https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/description/

Given an array arr, replace every element in that array with the greatest element among the elements to its right,
and replace the last element with -1.
After doing so, return the array.

Example 1:
Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
Explanation:
- index 0 --> the greatest element to the right of index 0 is index 1 (18).
- index 1 --> the greatest element to the right of index 1 is index 4 (6).
- index 2 --> the greatest element to the right of index 2 is index 4 (6).
- index 3 --> the greatest element to the right of index 3 is index 4 (6).
- index 4 --> the greatest element to the right of index 4 is index 5 (1).
- index 5 --> there are no elements to the right of index 5, so we put -1.

Example 2:
Input: arr = [400]
Output: [-1]
Explanation: There are no elements to the right of index 0.
Hint 1
Loop through the array starting from the end.
Hint 2
Keep the maximum value seen so far.
'''

# Runtime 544 ms Beats 58.90% of users with Python
# Memory 13.72 MB Beats 8.82% of users with Python

def replaceElements(arr):
    """
    :type arr: List[int]
    :rtype: List[int]
    """
    ll = len(arr);    narr = [0] * ll
    if ll == 1: return [-1]
    narr[ll - 1] = -1;
    mmax = -1
    for i in range(ll - 2, -1, -1):
        mmax=max(mmax,arr[i+1])
        narr[i]=mmax
        # narr[i] = max(narr[i + 1], arr[i + 1])
    return narr


#  Time Limit Exceeded  87 / 90 testcases passed
def replaceElements3(arr):
    """
    :type arr: List[int]
    :rtype: List[int]
    """
    ll=len(arr)
    if ll==1: return [-1]
    for i in range(ll-1):
        arr[i]=max(arr[i+1:])
    arr[ll-1]=-1
    return arr

def replaceElement2(arr):
    ll = len(arr)
    if ll == 1: return [-1]
    res = [max(arr[i + 1:]) for i in range(ll - 1)]
    res.append(-1)
    return res

print(replaceElements([17,18,5,4,6,1]))
