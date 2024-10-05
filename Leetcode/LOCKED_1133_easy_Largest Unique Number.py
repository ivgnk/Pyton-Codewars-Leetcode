"""
Done 05.09.2024. Topics: Hash Table, Sorting
1133. Largest Unique Number
Given an array of integers called nums, we are to find the highest value integer
that appears exactly once in the array.
If all integers appear more than once or if the array is empty,
the function should return -1.
https://algo.monster/liteproblems/1133
"""

from collections import Counter

def largestUniqueNumber(nums: list) -> int:
    if nums==[]: return -1
    n=sorted(nums,reverse=True)
    dd=dict(Counter(nums))
    for n1 in n:
        if dd[n1]==1: return n1
    return -1

print(largestUniqueNumber([4, 6, 2, 6, 4]))
print(largestUniqueNumber([4, 6, 2, 6, 4, 0]))
print(largestUniqueNumber([4, 6, 2, 6, 4, 0, 12]))


def largestUniqueNumber2(nums: list[int]) -> int:
    # Count the occurrences of each number in nums
    # using a Counter, which is a dictionary subclass
    number_counts = Counter(nums)

    # Traverse the range from 1000 (inclusive) to -1 (exclusive)
    # in descending order to find the largest unique number
    for num in range(1000, -1, -1):
        # Check if the number appears exactly once
        if number_counts[num] == 1:
            # If the number is unique, return it
            return num

    # Return -1 if no unique number is found
    return -1