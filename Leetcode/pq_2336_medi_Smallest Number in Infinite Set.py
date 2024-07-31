"""
Done 29.07.2024. Topics: Heap (Priority Queue)
You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].
Implement the SmallestInfiniteSet class:
SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
int popSmallest() Removes and returns the smallest integer contained in the infinite set.
void addBack(int num) Adds a positive integer num back into the infinite set,
if it is not already in the infinite set.


Example 1:
Input
["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
[[], [2], [], [], [], [1], [], [], []]
Output
[null, null, 1, 2, 3, null, 1, 4, 5]
Explanation
SmallestInfiniteSet smallestInfiniteSet = new SmallestInfiniteSet();
smallestInfiniteSet.addBack(2);    // 2 is already in the set, so no change is made.
smallestInfiniteSet.popSmallest(); // return 1, since 1 is the smallest number, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 2, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 3, and remove it from the set.
smallestInfiniteSet.addBack(1);    // 1 is added back to the set.
smallestInfiniteSet.popSmallest(); // return 1, since 1 was added back to the set and
                                   // is the smallest number, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 4, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 5, and remove it from the set.

Constraints:
1 <= num <= 1000
At most 1000 calls will be made in total to popSmallest and addBack.
"""

import heapq
# https://docs-python.ru/standart-library/modul-heapq-python

# Python
# Runtime 166 ms Beats 35.47%
# Memory 12.14 MB Beats 81.35%
# Python 3
# Runtime 163 ms Beats 17.82%
# Memory 17.38 MBBeats 17.35%

class SmallestInfiniteSet(object):

    def __init__(self):
        self.the_set=[i for i in range(1,1001)]
        # heapq.heapify(self.the_set)

    def popSmallest(self):
        """
        :rtype: int
        """
        return heapq.heappop(self.the_set)

    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num not in self.the_set:
            heapq.heappush(self.the_set, num)



# Runtime 187 ms Beats 27.52% Analyze Complexity
# Memory 12.19 MB Beats 81.35%
class SmallestInfiniteSet2(object):

    def __init__(self):
        self.the_set=[i for i in range(1,1002)]
        heapq.heapify(self.the_set)

    def popSmallest(self):
        """
        :rtype: int
        """
        return heapq.heappop(self.the_set)

    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num not in self.the_set:
            heapq.heappush(self.the_set, num)

