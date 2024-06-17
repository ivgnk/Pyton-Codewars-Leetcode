"""
Done 17.06.2024. Topics: Array
2644. Find the Maximum Divisibility Score

You are given two integer arrays nums and divisors.
The divisibility score of divisors[i] is the number of indices j such that nums[j] is divisible by divisors[i].
Return the integer divisors[i] with the maximum divisibility score.
If multiple integers have the maximum score, return the smallest one.

Example 1:
Input: nums = [2,9,15,50], divisors = [5,3,7,2]
Output: 2
Explanation:
The divisibility score of divisors[0] is 2 since nums[2] and nums[3] are divisible by 5.
The divisibility score of divisors[1] is 1 since only nums[1] is divisible by 3.
The divisibility score of divisors[2] is 0 since none of the numbers in nums is divisible by 7.
The divisibility score of divisors[3] is 2 since nums[0] and nums[3] are divisible by 2.
As divisors[0] and divisors[3] have the same divisibility score, we return the smaller one which is divisors[3].

Example 2:
Input: nums = [4,7,9,3,9], divisors = [5,2,3]
Output: 3
Explanation:
The divisibility score of divisors[0] is 0 since none of numbers in nums is divisible by 5.
The divisibility score of divisors[1] is 1 since only nums[0] is divisible by 2.
The divisibility score of divisors[2] is 3 since nums[2], nums[3] and nums[4] are divisible by 3.

Example 3:
Input: nums = [20,14,21,10], divisors = [10,16,20]
Output: 10
Explanation:
The divisibility score of divisors[0] is 0 since none of the numbers in nums is divisible by 10.
The divisibility score of divisors[1] is 0 since none of the numbers in nums is divisible by 16.
The divisibility score of divisors[2] is 0 since none of the numbers in nums is divisible by 20.
As divisors[0], divisors[1] and divisors[2] all have the same divisibility score, we return the smallest one which is divisors[0].

Hint 1
Consider counting for each element in divisors the count of elements in nums divisible by it using bruteforce.
Hint 2
After counting for each divisor, take the one with the maximum count. In case of a tie, take the minimum one of them.
"""


# Runtime 5800 ms Beats 6.67%
# Memory 12.06 MB Beats 6.67%
def maxDivScore2(nums, divisors):
    """
    :type nums: List[int]
    :type divisors: List[int]
    :rtype: int
    """
    lld=len(divisors); rlld=range(lld)
    lln=len(nums)
    res=[[0,divisors[i]] for i in rlld]
    # print(res)
    for i in rlld:
        for j in range(lln):
            n=nums[j]%divisors[i]
            if n==0: res[i][0]+=1
    # print(res)
    res=sorted(res,reverse=True,key=lambda x:(x[0],-x[1]))
    return res[0][1]

# Runtime 3406 ms Beats 26.67%
# Memory 11.90 MB Beats 57.78%

def maxDivScore(nums, divisors):
    """
    :type nums: List[int]
    :type divisors: List[int]
    :rtype: int
    """
    mx = 0; res = []
    for divi in divisors:
        tmx = 0
        for i in nums:
            if i % divi == 0:
                tmx += 1
        if tmx > mx:
            res = [divi]
            mx = tmx
        elif tmx == mx:
            res.append(divi)
            mx = tmx
    return min(res)


# print(maxDivScore(nums = [2,9,15,50], divisors = [5,3,7,2])) # 2
# print(maxDivScore( nums = [4,7,9,3,9], divisors = [5,2,3])) # 3
print(maxDivScore(nums = [20,14,21,10], divisors = [10,16,20])) # 10
