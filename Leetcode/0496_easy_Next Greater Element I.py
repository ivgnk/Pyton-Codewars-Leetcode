"""
Done 09.05.2024. Topics: Array, Hash Table, Stack, Monotonic Stack
496. Next Greater Element I
https://leetcode.com/problems/next-greater-element-i/description/

The next greater element of some element x in an array is the first greater element
that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2,
where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and
determine the next greater element of nums2[j] in nums2.
If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.
length such that ans[i] is the next greater element as described above.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.

Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.
"""

# Runtime 224 ms Beats 6.22% of users with Python
# Memory 11.87 MB Beats 66.55% of users with Python

def nextGreaterElement2(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    l1= len(nums1); ans = []; ans2=[-1]*l1
    l2 = len(nums2)
    for i in range(l1):
        for j in range(l2):
            if nums1[i] == nums2[j]:
                ans.append(j)
    for i,j in enumerate(ans):
        for k in range(j+1,l2):
            if nums2[j]<nums2[k]:
                ans2[i]=nums2[k]
                break
    return  ans2

# Runtime 226 ms Beats 6.04% of users with Python
# Memory 11.76 MB Beats 91.70% of users with Python
def nextGreaterElement3(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    l1 = len(nums1); ans2 = [-1] * l1
    rl1 = range(l1)
    l2 = len(nums2)
    ans = [j for i in rl1
           for j in range(l2)
                if nums1[i] == nums2[j]]

    for i in rl1:
        j = ans[i]
        for k in range(j + 1, l2):
            if nums2[j] < nums2[k]:
                ans2[i] = nums2[k]
                break

    return ans2

# Runtime 172 ms Beats 9.38% of users with Python
# Memory 11.94 MB Beats 31.83% of users with Python
# Runtime 154 ms Beats 11.18% of users with Python
# Memory 11.91 MB Beats 31.83% of users with Python

def nextGreaterElement4(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    l1 = len(nums1); ans2 = [-1] * l1
    rl1 = range(l1)
    l2 = len(nums2)
    pr = False
    for i in rl1:
        for j in range(l2):
            if nums1[i] == nums2[j]:
                for k in range(j+1,l2):
                    if nums2[k]>nums2[j]:
                        pr=True
                        ans2[i]=nums2[k]
                        break
                if pr:
                    pr = False
                    break
    return ans2

# decision by https://leetcode.com/adarshg04/
# Runtime 30 ms Beats 66.37% of users with Python
# Memory 11.97 MB Beats 31.83% of users with Python
def nextGreaterElement5(nums1, nums2):
    ans=[]
    for i in nums1:
        ind=nums2.index(i)
        while ind<len(nums2):
            if i < nums2[ind]:
                ans.append(nums2[ind])
                break
            ind=ind+1
        else:
            ans.append(-1)
    return ans

# my decision based on  https://leetcode.com/adarshg04/
# Runtime 45 ms Beats 36.97% of users with Python
# Memory 11.58 MB Beats 100.00% of users with Python
def nextGreaterElement(nums1, nums2):
    ans=[]
    for dat in nums1:
        ind=nums2.index(dat)
        for j in range(ind+1,len(nums2)):
            if nums2[j]>dat:
                ans.append(nums2[j])
                break
        else:
            ans.append(-1)
    return ans

print(nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2]))
# print(nextGreaterElement(nums1 = [2,4], nums2 = [1,2,3,4]))




