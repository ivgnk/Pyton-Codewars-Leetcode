"""
Done 19.12.2024. Topics: Greedy
769. Max Chunks To Make Sorted
https://leetcode.com/problems/max-chunks-to-make-sorted/

You are given an integer array arr of length n that represents a
permutation of the integers in the range [0, n - 1].

We split arr into some number of chunks (i.e., partitions), and individually sort each chunk.
After concatenating them, the result should equal the sorted array.

Return the largest number of chunks we can make to sort the array.

Example 1:
Input: arr = [4,3,2,1,0]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.

Example 2:
Input: arr = [1,0,2,3,4]
Output: 4
Explanation:
We can split into two chunks, such as [1, 0], [2, 3, 4].
However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.

Constraints:
n == arr.length
1 <= n <= 10
0 <= arr[i] < n
All the elements of arr are unique.

Hint 1
The first chunk can be found as the smallest k for which A[:k+1] == [0, 1, 2, ...k];
then we repeat this process.

The best way to do this is to think that as all the numbers are unique and we know the size of array, so we know
all elements in the array. so, we know that in the sorted array arr[i] = i,
it means that if we compute a running sum of elements in the array,
then if at any moment, the sum = i*(i+1)/2,
then we should make a partition at that point.
continuing this process will give us the max no. of partitions.
like : 1, 0, 2, 3, 4
running sum : 1, 1, 3, 6, 10
i*(i+1)/2 : 0, 1, 3, 6, 10
for this, sum = i*(i+1)/2 condition is correct 4 times, so answer is 4
https://leetcode.com/problems/max-chunks-to-make-sorted/description/comments/2275989

Me solution https://leetcode.com/problems/max-chunks-to-make-sorted/solutions/6163697/easy-python-solution-for-problem-0769-ba-op6p/
✏️ Easy Python solution for Problem 0769, based on tips
"""

# Runtime 0 ms Beats 100.00%
# Memory 12.36 MB Beats 11.27%
# Time Complexity O(N)
# Space Complexity O(1)
def maxChunksToSorted(arr):
    """
    :type arr: List[int]
    :rtype: int
    """
    rs=0; n2=0
    for i in range(len(arr)):
        n=i*(i+1)/2
        rs+=arr[i]
        if n==rs:
            n2+=1
    return n2

if __name__=="__main__":
    print(maxChunksToSorted([4,3,2,1,0]))
    print(maxChunksToSorted([1,0,2,3,4]))


