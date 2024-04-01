'''
1437. Check If All 1's Are at Least Length K Places Away
https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/description/

Given an binary array nums and an integer k,
return true if all 1's are at least k places away from each other, otherwise return false.

Example 1:
Input: nums = [1,0,0,0,1,0,0,1], k = 2
Output: true
Explanation: Each of the 1s are at least 2 places away from each other.

Example 2:
Input: nums = [1,0,0,1,0,1], k = 2
Output: false
Explanation: The second 1 and third 1 are only one apart from each other.
'''


# def kLengthApart3(nums, k):
#     """
#     :type nums: List[int]
#     :type k: int
#     :rtype: bool
#     """
#     ll=len(nums)
#     st=1
#     if nums[0]==0:
#         n=1
#         for i in range(1,ll):
#             if nums[i]==0: n=n+1
#             else:
#                 if n<=k: return False
#                 else: st=i
#     print(st)
#     first0=-1; next0=-1
#     for i in range(st,ll):
#         if nums[i]==0:
#             if first0<0:
#                 first0=i
#             else:
#                 next0=i
#         else: # ones
#             if next0-first0+1<k:
#                 print(first0,next0)
#                 return False
#             else: first0=-1;
#     return True

# def kLengthApart2(self, nums, k):
#     """
#     :type nums: List[int]
#     :type k: int
#     :rtype: bool
#     """
#     first0=-1; next0=-1
#     for i in range(1,len(nums)):
#         if nums[i]==0:
#             if first0<0:
#                 first0=i
#             else:
#                 next0=i
#         else: # ones
#             if next0-first0+1<k:
#                 # print(first0,next0)
#                 return False
#             else: first0=-1;
#     return True


# print(kLengthApart(nums = [1,0,0,0,1,0,0,1], k = 2))
# print(kLengthApart(nums = [1,0,0,0,1,0,1], k = 2))

def kLengthApart(nums, k):
    ll = len(nums)
    s = ''.join(str(dat) for dat in nums)
    # print(s)
    s2 = s.split('1')
    print('s2=', s2)
    s3 = [len(dat) for dat in s2]
    print('s3=', s3)
    s4 = [value for value in s3 if value]
    print('s4 (1)=', s4)
    if s4 == [] and k == 0: return True
    if len(s4) == 1: return s4[0] >= k
    if nums[0] == 0: s4 = s4[1:]
    if nums[ll - 1] == 0 and s4[-1] == 1: s4 = s4[:-1]
    print('s4 (2)=', s4)
    return min(s4) >= k


# print(kLengthApart(nums = [1,0,0,0,0,1,0,0,0,1,0,0,1,0,1], k =1))
# print(kLengthApart(nums = [1,1,1,1,1], k =0))
print(kLengthApart(nums = [1,0,0,0,1,0,0,1,0], k =2))