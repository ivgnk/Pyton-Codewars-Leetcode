"""
Done 12.08.2024. Topics: Sorting, Bisect
703. Kth Largest Element in a Stream
https://leetcode.com/problems/kth-largest-element-in-a-stream/

Design a class to find the kth largest element in a stream.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:
KthLargest(int k, int[] nums)
Initializes the object with the integer k and the stream of integers nums.

int add(int val)
Appends the integer val to the stream and returns the element representing the kth largest element in the stream.

Example 1:
Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]
Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8


Constraints:
1 <= k <= 104
0 <= nums.length <= 104
-104 <= nums[i] <= 104
-104 <= val <= 104
At most 104 calls will be made to add.
It is guaranteed that there will be at least k elements in the array when you search for the kth element.

https://docs.python.org/3/library/heapq.html

Solution
✏️ Not easy Python solution with 5 tricks

Intuition
At first glance, everything is simple.

Approach
First, the wrong trick: use only Heap (Priority Queue), as specified in Topics.
But there is a nuance. You will get "Time Limit Exceeded - 9 / 10 testcases passed".

Main tricks (the task is most likely of medium
level):
1) Do not use Heap (Priority Queue) !!!
2) Sort the array at the very beginning and store the sorted values (without using Priority Queue)
3) Use storing the k-maximum value, and not calculating it again. In this case, you need to take into account some extreme cases, for example, when the original array is empty or its length is less than k.
4) Insert values into the array that are greater than the k-maximum. Tricks 1+2+3+4 will give Runtime about 700 ms. But higher speed is needed.
5) To insert into a sorted array, use the insort function from the bisect module.

Execution August 12, 2024: Runtime 78 ms Beats 90.90%
"""

# stackoverflow.com/questions/8024571/insert-an-item-into-sorted-list-in-python
import bisect
# Runtime 720 ms Beats 11.22% Analyze Complexity
# Memory 16.27 MB Beats 9.63%
class KthLargest3(object):
    def __init__(self, k, nums):
        self.k=k
        self.nums=sorted(nums)
        self.len=len(self.nums)
        if self.len>0 and self.len>=k:
            self.kth=self.nums[-k]
        else:
            self.kth = None

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if self.kth:
            if val>self.kth:
                self.nums.append(val)
                self.nums=sorted(self.nums)
        else:
            self.nums.append(val)
            self.nums = sorted(self.nums)

        self.kth = self.nums[-self.k]
        return self.kth

        # Your KthLargest object will be instantiated and called as such:

# Time Limit Exceeded - 9 / 10 testcases passed
import heapq
class KthLargest2(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k=k
        self.nums=[-x for x in nums]
        heapq.heapify(self.nums)


    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.nums, -val)
        kth=heapq.nsmallest(self.k, self.nums, key=None)
        return -kth[-1]


# Time Limit Exceeded - 9 / 10 testcases passed
class KthLargest4(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k=k
        self.nums=[-x for x in nums]
        heapq.heapify(self.nums)
        self.len=len(self.nums)
        if self.len>0 and self.len>=k:
            kth = heapq.nsmallest(self.k, self.nums, key=None)
            self.kth = -kth[-1]
        else:
            self.kth = None
        print('init ',self.kth,self.k)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if self.kth:
            if val>self.kth:
                heapq.heappush(self.nums, -val)
                kth=heapq.nsmallest(self.k, self.nums, key=None)
                self.kth=-kth[-1]
                return self.kth
            else: return self.kth
        else:
            heapq.heappush(self.nums, -val)
            kth = heapq.nsmallest(self.k, self.nums, key=None)
            self.kth = -kth[-1]
            return self.kth


# Runtime 78 ms Beats 90.90%
# Memory 16.13 MB Beats 9.63%
class KthLargest(object):
    def __init__(self, k, nums):
        self.k=k
        self.nums=sorted(nums)
        self.len=len(self.nums)
        if self.len>0 and self.len>=k:
            self.kth=self.nums[-k]
        else:
            self.kth = None

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if self.kth:
            if val>self.kth:
                    bisect.insort(self.nums,val)
        else:
            bisect.insort(self.nums, val)

        self.kth = self.nums[-self.k]
        return self.kth


def tst_01():
    obj = KthLargest(3, [4, 5, 8, 2])
    # in: [3], [5], [10], [9], [4]
    # Out:  4, 5, 5, 8, 8
    param_1 = obj.add(3); print(param_1)
    param_1 = obj.add(5); print(param_1)
    param_1 = obj.add(10); print(param_1)
    param_1 = obj.add(9); print(param_1)
    param_1 = obj.add(4); print(param_1)

def tst_02():
    obj = KthLargest(1, [])
    param_1 = obj.add(-3); print(param_1)
    param_1 = obj.add(-2); print(param_1)
    param_1 = obj.add(-4); print(param_1)
    param_1 = obj.add(0); print(param_1)
    param_1 = obj.add(4); print(param_1)

def tst_03():
    obj = KthLargest(2, [0])
    param_1 = obj.add(-1); print(param_1)
    param_1 = obj.add(1); print(param_1)
    param_1 = obj.add(-2); print(param_1)
    param_1 = obj.add(-4); print(param_1)
    param_1 = obj.add(3); print(param_1)
tst_03()

