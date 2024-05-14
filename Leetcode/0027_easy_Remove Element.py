"""
Done 14.05.2024. Topics: Array, Two Pointers
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted,
you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:
The judge will test your solution with the following code:
int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

Hint 1
The problem statement clearly asks us to modify the array in-place and
it also says that the element beyond the new length of the array can be anything.
Given an element, we need to remove all the occurrences of it from the array.
We don't technically need to remove that element per-say, right?
Hint 2
We can move all the occurrences of this element to the end of the array. Use two pointers!

Hint 3
Yet another direction of thought is to consider the elements to be removed as non-existent.
In a single pass, if we keep copying the visible elements in-place,
that should also solve this problem for us.
"""

# Runtime 5 ms Beats 99.13% of users with Python
# Memory 11.72 MB Beats 10.73% of users with Python

def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    n=nums.count(val); ll=len(nums)

    n2i=ll-n
    n2 = [i for i in nums if i!=val]
    for i,dat in enumerate(n2):
        nums[i]=n2[i]
    return  n2i
