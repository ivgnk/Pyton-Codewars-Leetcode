"""
Done 02.08.2024. Topics: Array, Sliding Window

2134. Minimum Swaps to Group All 1's Together II
https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii

A swap is defined as taking two distinct positions in an array and swapping the values in them.

A circular array is defined as an array where we consider the first element and the last element to be adjacent.

Given a binary circular array nums, return the minimum number of swaps required to group all 1's
present in the array together at any location.

Example 1:
Input: nums = [0,1,0,1,1,0,0]
Output: 1
Explanation: Here are a few of the ways to group all the 1's together:
[0,0,1,1,1,0,0] using 1 swap.
[0,1,1,1,0,0,0] using 1 swap.
[1,1,0,0,0,0,1] using 2 swaps (using the circular property of the array).
There is no way to group all 1's together with 0 swaps.
Thus, the minimum number of swaps required is 1.

Example 2:
Input: nums = [0,1,1,1,0,0,1,1,0]
Output: 2
Explanation: Here are a few of the ways to group all the 1's together:
[1,1,1,0,0,0,0,1,1] using 2 swaps (using the circular property of the array).
[1,1,1,1,1,0,0,0,0] using 2 swaps.
There is no way to group all 1's together with 0 or 1 swaps.
Thus, the minimum number of swaps required is 2.

Example 3:
Input: nums = [1,1,0,0,1]
Output: 0
Explanation: All the 1's are already grouped together due to the circular property of the array.
Thus, the minimum number of swaps required is 0.

Constraints:
1 <= nums.length <= 105
nums[i] is either 0 or 1.

Hint 1
Notice that the number of 1’s to be grouped together is fixed. It is the number of 1's the whole array has.
Hint 2
Call this number total. We should then check for every subarray of size total (possibly wrapped around),
how many swaps are required to have the subarray be all 1’s.
Hint 3
The number of swaps required is the number of 0’s in the subarray.
Hint 4
To eliminate the circular property of the array, we can append the original array to itself.
Then, we check each subarray of length total.
Hint 5
How do we avoid recounting the number of 0’s in the subarray each time? The Sliding Window technique can help.

Four Hints if you want them!
https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/description/comments/1891292
Hint 1:
Use a sliding window

Hint 2:
Sliding window should be the size of the total number of 1s

Hint 3:
The number of 0s within the window is the swap count

Hint 4:
Easiest way for a sliding window to work with a circular array is to expand the array to include the beginning elements (up to the window size) at the end of a new search array. For example, take this example:

[0,1,1,1,0,0,1,1,0]

There are 5 ones so our window is 5. We can add the first 5 to the end of this array:

[0,1,1,1,0,0,1,1,0,0,1,1,1,0]

Now we can search as if it were circular.
It would probably be faster to not build out this new array and do some calculations when near the end of the original array but this is the most simple approach.

as hint 2
the maximum of the sliding window is the number of 1s in nums
the number of swaps is the number of 0s in the window, which has the largest number of 1s.
https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/description/comments/2552644
"""

# Runtime 642 ms Beats 96.55%
# Time Complexity O(N)
# Memory 18.60 MB Beats 41.38%
# Space Complexity O(1)


def minSwaps(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ll = len(nums)
    n1 = nums.count(1)
    if n1 == 0: return 0
    s = nums[0:n1]
    n11=n1 - 1
    nums = nums + s
    nn_1 = s.count(1)
    s = sum(nums[0:n1])
    for i in range(1, ll):
        s-=nums[i-1]
        s = s + nums[i + n11]
        nn_1 = max(nn_1, s)
    return n1 - nn_1

print(minSwaps([0,1,0,1,1,0,0]))
print(minSwaps([0,1,1,1,0,0,1,1,0]))
print(minSwaps( [1,1,0,0,1]))


from icecream import ic
def minSwaps2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ll=len(nums)
    n1=nums.count(1)
    # ic(nums)
    nums=nums+nums[:n1]
    # ic(nums)
    s = nums[0:n1]
    # ic(0,s)
    nn_1=[s.count(1)]
    for i in range(1, ll):
        s.pop(0)
        s = s+[nums[i+n1-1]]
        # ic(i,i+n1-1,nums[i+n1-1],s,s.count(1))
        nn_1.append(s.count(1))
    # ic(nn_1)
    return n1-max(nn_1)

def minSwaps3(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ll = len(nums)
    n1 = nums.count(1)
    if n1 == 0: return 0
    s = nums[0:n1]
    n11=n1 - 1
    nums = nums + s
    nn_1 = s.count(1)
    for i in range(1, ll):
        s.pop(0)
        s = s + [nums[i + n11]]
        nn_1 = max(nn_1, s.count(1))
    return n1 - nn_1

# Memory Limit Exceeded - 49 / 63 testcases passed
def minSwaps1(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ll=len(nums)
    n1=nums.count(1)
    nums=nums+nums[:n1]
    nn_1=[nums[i:i+n1] for i in range(ll)]
    nn1=[nn_1[i].count(1) for i in range(ll)]
    return n1-max(nn1)

