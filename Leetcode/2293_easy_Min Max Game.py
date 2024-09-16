"""
Done 16.09.2024. Topics: Array, Simulation
2293. Min Max Game
https://leetcode.com/problems/min-max-game/description/

You are given a 0-indexed integer array nums whose length is a power of 2.

Apply the following algorithm on nums:

Let n be the length of nums. If n == 1, end the process.
Otherwise, create a new 0-indexed integer array newNums of length n / 2.
For every even index i where 0 <= i < n / 2, assign the value of newNums[i] as min(nums[2 * i], nums[2 * i + 1]).
For every odd index i where 0 <= i < n / 2, assign the value of newNums[i] as max(nums[2 * i], nums[2 * i + 1]).
Replace the array nums with newNums.
Repeat the entire process starting from step 1.
Return the last number that remains in nums after applying the algorithm.

Example 1:
Input: nums = [1,3,5,2,4,8,2,2]
Output: 1
Explanation: The following arrays are the results of applying the algorithm repeatedly.
First: nums = [1,5,4,2]
Second: nums = [1,4]
Third: nums = [1]
1 is the last remaining number, so we return 1.

Example 2:
Input: nums = [3]
Output: 3
Explanation: 3 is already the last remaining number, so we return 3.

Constraints:
1 <= nums.length <= 1024
1 <= nums[i] <= 109
nums.length is a power of 2.

Hint 1
Simply simulate the algorithm.
Hint 2
Note that the size of the array decreases exponentially, so the process will terminate after just O(log n) steps.
"""

# Runtime 39 ms Beats 26.25%
# Memory 11.88 MB Beats 33.75%

def minMaxGame(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ll = len(nums)
    while ll > 1:
        nums = [min(nums[i * 2], nums[i * 2 + 1]) if i % 2 == 0 else max(nums[i * 2], nums[i * 2 + 1]) for i in
                range(0, ll // 2)]
        ll = ll // 2
    return nums[0]


# Runtime 45 ms Beats 8.75%
# Memory 11.86 MB Beats 33.75%
def minMaxGame5(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ll=len(nums)
    while ll>1:
        nums=[min(nums[i*2], nums[i*2 + 1]) if i%2==0 else max(nums[i*2], nums[i*2 + 1]) for i in range(0,ll//2) ]
        ll=len(nums)
    return nums[0]
print(minMaxGame([1,3,5,2,4,8,2,2])) # 1
print(minMaxGame([3]))


# Runtime 50 ms Beats 7.50%
# Memory 11.75 MB Beats 63.75%
def minMaxGame3(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ll=len(nums)
    while ll>1:
        nn=[]
        for i in range(0,ll//2):
            i2=2*i
            if i%2==0:
                nn.append(min(nums[i2], nums[i2 + 1]))
            else:
                nn.append(max(nums[i2], nums[i2 + 1]))
        nums=nn
        ll=len(nums)
    return nums[0]

# Runtime 61 ms Beats 6.25%
# Memory 11.80 MB Beats 33.75%
def minMaxGame2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ll=len(nums)
    while ll>1:
        nn=[]
        for i in range(0,ll//2):
            if i%2==0:
                nn.append(min(nums[2 * i], nums[2 * i + 1]))
            else:
                nn.append(max(nums[2 * i], nums[2 * i + 1]))
        nums=nn
        ll=len(nums)
    return nums[0]

