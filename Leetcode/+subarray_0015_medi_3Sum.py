'''
16.06.2024. Topics: Array, Two Pointers, Sorting
15. 3Sum
https://leetcode.com/problems/3sum/description/
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.


Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Hint 1
So, we essentially need to find three numbers x, y, and z such that they add up to the given value.
If we fix one of the numbers say x, we are left with the two-sum problem at hand!
Hint 2
For the two-sum problem, if we fix one of the numbers, say x,
we have to scan the entire array to find the next number y, which is value - x where value is the input parameter.
Can we change our array somehow so that this search becomes faster?
Hint 3
The second train of thought for two-sum is, without changing the array, can we use additional space somehow?
Like maybe a hash map to speed up the search?
'''

import itertools

# Time Limit Exceeded -- 270 / 313 testcases passed
def threeSum2(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    # How do I generate all permutations of a list?
    # https://stackoverflow.com/questions/104420/how-do-i-generate-all-permutations-of-a-list

    # Good, but Time Limit Exceeded
    llst = list(itertools.permutations(nums, 3))
    # print(f'{llst=} \n{len(llst)=}')
    rlst = set()
    for i,lis in enumerate(llst):
        if (lis[0]+lis[1]+lis[2])==0:
            a= list(lis)
            a.sort()
            # print(i,a)
            rlst.add(tuple(a))
    return list(rlst)

# print('res=',threeSum2([-1,0,1,2,-1,-4]))


# Time Limit Exceeded -- 308 / 313 testcases passed
# ll = 3000
def threeSum3(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    ll = len(nums)
    res = []
    nums = sorted(nums)
    print(ll)
    rll = range(ll)
    for i in rll:
        for j in rll:
            if i != j:
                ss = nums[i] + nums[j]
                for k in rll:
                    if j != k:
                        if i != k:
                            if ss == -nums[k]:
                                res.append(tuple(sorted([nums[i], nums[j], nums[k]])))
    return list(set(res))

# Time Limit Exceeded -- 308 / 313 testcases passed
def threeSum4(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    ll=len(nums); res=[]; nums=sorted(nums)
    rll=range(ll)
    for i in rll:
        for j in range(i+1,ll-1):
            ss = nums[i] + nums[j]
            for k in range(j+1,ll):
                if ss == -nums[k]:
                    res.append(tuple(sorted([nums[i], nums[j], nums[k]])))
    return list(set(res))

# Не работает, тк. м.б несколько отрицательных давать одно положительное
def threeSum5(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    ll = len(nums);    res = [];
    nums = sorted(nums)
    rll = range(ll);    ll1 = ll - 1
    print(nums)

    dx = [i for i in rll if nums[i] < 0]
    ldx = len(dx)
    if ldx == 0:
        all0 = all([nums[i] == 0 for i in rll])
        if not all0:
            return res
        else:
            pdx = 0
    else:
        pdx = dx[-1] + 1

    for i in range(pdx, ll):
        for j in range(i + 1, ll1):
            ss = nums[i] + nums[j]
            if ldx == 0:
                ndx = j + 1
            else:
                ndx = dx[0]
            print(i, j, ndx, pdx)
            for k in range(ndx, ll):
                if ss == -nums[k]:
                    res.append(tuple(sorted([nums[i], nums[j], nums[k]])))
    return list(set(res))


from icecream import ic

# https://leetcode.com/problems/3sum/solutions/5311175/best-python-3sum-solution-sorting-two-pointers
# Runtime 847 ms Beats 65.62%
# Memory 14.88 MB Beats 85.66%
# Space Complexity O(1)
# Time Complexity O(N**2)

def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums.sort()  # Step 1: Sort the array
    res = []  # Initialize the result list
    n = len(nums)  # Get the length of the array

    for i in range(n):
        # Step 3: Skip duplicates for the current position
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, n - 1  # Initialize two pointers

        while left < right:  # Process with the two-pointer technique
            total = nums[i] + nums[left] + nums[right]  # Calculate the sum
            if total < 0:  # If the sum is less than zero
                left += 1  # Increment the left pointer
            elif total > 0:  # If the sum is greater than zero
                right -= 1  # Decrement the right pointer
            else:  # If the sum is zero
                res.append([nums[i], nums[left], nums[right]])  # Add the triplet to the result
                left += 1  # Move the left pointer
                right -= 1  # Move the right pointer

                # Step 5: Skip duplicates for the left pointer
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                # Step 5: Skip duplicates for the right pointer
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

    return res  # Step 6: Return the result list

ic(threeSum([-1,0,1,2,-1,-4]))