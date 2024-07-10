"""
Done 10.07.2024. Topics: Array, Simulation
2899. Last Visited Integers
https://leetcode.com/problems/last-visited-integers/description/

Given an integer array nums where nums[i] is either a positive integer or -1.
We need to find for each -1 the respective positive integer, which we call the last visited integer.

To achieve this goal, let's define two empty arrays: seen and ans.

Start iterating from the beginning of the array nums.

If a positive integer is encountered, prepend it to the front of seen.
If -1 is encountered, let k be the number of consecutive -1s seen so far (including the current -1),
If k is less than or equal to the length of seen, append the k-th element of seen to ans.
If k is strictly greater than the length of seen, append -1 to ans.
Return the array ans.



Example 1:
Input: nums = [1,2,-1,-1,-1]
Output: [2,1,-1]
Explanation:
Start with seen = [] and ans = [].
Process nums[0]: The first element in nums is 1. We prepend it to the front of seen.
Now, seen == [1].
Process nums[1]: The next element is 2. We prepend it to the front of seen.
Now, seen == [2, 1].
Process nums[2]: The next element is -1. This is the first occurrence of -1, so k == 1.
We look for the first element in seen. We append 2 to ans.
Now, ans == [2].
Process nums[3]: Another -1. This is the second consecutive -1, so k == 2.
The second element in seen is 1, so we append 1 to ans.
Now, ans == [2, 1].
Process nums[4]: Another -1, the third in a row, making k = 3.
However, seen only has two elements ([2, 1]).
Since k is greater than the number of elements in seen, we append -1 to ans.
Finally, ans == [2, 1, -1].

Example 2:
Input: nums = [1,-1,2,-1,-1]
Output: [1,2,1]
Explanation:
Start with seen = [] and ans = [].

Process nums[0]: The first element in nums is 1.
We prepend it to the front of seen.
Now, seen == [1].
Process nums[1]: The next element is -1. This is the first occurrence of -1, so k == 1.
We look for the first element in seen, which is 1.
Append 1 to ans. Now, ans == [1].
Process nums[2]: The next element is 2.
Prepend this to the front of seen.
Now, seen == [2, 1].
Process nums[3]: The next element is -1.
This -1 is not consecutive to the first -1 since 2 was in between.
Thus, k resets to 1. The first element in seen is 2, so append 2 to ans.
Now, ans == [1, 2].
Process nums[4]: Another -1. This is consecutive to the previous -1, so k == 2.
The second element in seen is 1, append 1 to ans.
Finally, ans == [1, 2, 1].

Constraints:
1 <= nums.length <= 100
nums[i] == -1 or 1 <= nums[i] <= 100

Hint 1
It is sufficient to implement what the description is stating.
"""

# Runtime 21 ms Beats 90.91%
# Memory 11.56 MB Beats 59.09%
# https://leetcode.com/problems/last-visited-integers/submissions/1315938596/

# Runtime 27 ms Beats 72.73%
# Memory 11.54 MB Beats 59.09%
# Runtime 26 ms Beats 75.00%
# Memory 11.68 MB Beats 25.00%
# Runtime 25 ms Beats 77.27%
# Memory 11.59 MB Beats 59.09%

def lastVisitedIntegers(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    seen = []; ans = []
    k=0; ll=0
    for i,n in enumerate(nums):
        # print(i,n,seen)
        if n>0:
            seen.insert(0,n)
            ll=ll+1
            k=0
        else:
            k=k+1
            if k>ll: ans.append(-1)
            else: ans.append(seen[k-1])
    return ans

print(lastVisitedIntegers([1,2,-1,-1,-1]))
print(lastVisitedIntegers([1,-1,2,-1,-1]))
