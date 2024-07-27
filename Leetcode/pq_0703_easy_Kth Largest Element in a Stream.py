"""
27.07.2024. Topics: Heap (Priority Queue)
703. Kth Largest Element in a Stream
https://leetcode.com/problems/kth-largest-element-in-a-stream/description/

Design a class to find the kth largest element in a stream.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:
KthLargest(int k, int[] nums) Initializes the object
with the integer k and the stream of integers nums.

int add(int val) Appends the integer val to the stream and
returns the element representing the kth largest element in the stream.

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
0 <= nums.length <= 10**4
-104 <= nums[i] <= 10**4
-104 <= val <= 10**4
At most 10**4 calls will be made to add.
It is guaranteed that there will be at least k elements in the array when you search for the kth element.
"""

# https://docs-python.ru/standart-library/modul-heapq-python/
import heapq

# Runtime 87 ms Beats 67.16%
# Memory 16.04 MB Beats 31.72%
# Runtime 80 ms Beats 89.46%
# Memory 16.14 MB Beats 9.42%
class KthLargest:
    def __init__(self, k, nums):
        self.heap = nums
        self.k = k
        heapq.heapify(self.heap)
        #  heappop() возвращает и удаляет наименьший элемент из кучи, сохраняя инвариант кучи.
        while len(self.heap)>self.k:
            heapq.heappop(self.heap)

    def add(self, val) -> int:
        heapq.heappush(self.heap,val[0]) # вставляем
        if len(self.heap)>self.k: # сразу удаляем ненужный элемент
            heapq.heappop(self.heap)
        return self.heap[0]

# Time Limit Exceeded - 9 / 10 testcases passed
class KthLargest2(object):
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        print('KthLargest2')
        self.k = k
        self.nums = [-i for i in nums]
        heapq.heapify(self.nums)
        print('init ',self.nums, '  ')

    def add(self, val:list):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.nums, -val[0])
        r = heapq.nsmallest(self.k, self.nums)
        print('add ',val,'  ',self.nums,'  ',r, r[-1])
        return -r[-1]


# Time Limit Exceeded - 9 / 10 testcases passed
class KthLargest3(object):
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        llen=len(nums)
        print(llen)
        self.k=k
        self.nums=[-i for i in nums]
        self.llen=llen
        heapq.heapify(self.nums)
        if self.llen>=k:
            self.kmax = - heapq.nsmallest(self.k, self.nums)[-1]
        else:
            self.kmax = 100000

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if self.llen<self.k:
            heapq.heappush(self.nums,-val)
            self.kmax = - heapq.nsmallest(self.k, self.nums)[-1]
            self.llen=self.llen+1
        elif self.kmax<val:
            heapq.heappush(self.nums,-val)
            self.kmax = - heapq.nsmallest(self.k, self.nums)[-1]
            self.llen=self.llen+1
        return self.kmax

        # return -r[0]


def tst_1():
    Kth = KthLargest2(3, [4, 5, 8, 2])
    Kth.add([3]); Kth.add([5]); Kth.add([10]); Kth.add([9]);    Kth.add([4])

    Kth = KthLargest(3, [4, 5, 8, 2])
    Kth.add([3]); Kth.add([5]); Kth.add([10]); Kth.add([9]);    Kth.add([4])

def tst_2():
    Kth = KthLargest2(1, [])
    Kth.add([-3]); Kth.add([-2]); Kth.add([-4]); Kth.add([0]); Kth.add([4])

def tst_3():
    Kth = KthLargest(3, [4, 5, 8, 2, 1, 0, 7 , 12])
    Kth.add([3]); Kth.add([5]); Kth.add([10]); Kth.add([9]);    Kth.add([4])

    Kth = KthLargest(1, [])
    Kth.add([-3]); Kth.add([-2]); Kth.add([-4]); Kth.add([0]); Kth.add([4])


tst_3()

