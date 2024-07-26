"""
26.07.2024. Topics: Concurrency
1114. Print in Order
https://leetcode.com/problems/print-in-order/description/

Suppose we have a class:

public class Foo {
  public void first() { print("first"); }
  public void second() { print("second"); }
  public void third() { print("third"); }
}
The same instance of Foo will be passed to three different threads.
Thread A will call first(), thread B will call second(), and thread C will call third().
Design a mechanism and modify the program to ensure that second() is executed after first(),
and third() is executed after second().

Note:
We do not know how the threads will be scheduled in the operating system, even though the numbers
in the input seem to imply the ordering.
The input format you see is mainly to ensure our tests' comprehensiveness.

Example 1:
Input: nums = [1,2,3]
Output: "firstsecondthird"
Explanation: There are three threads being fired asynchronously. The input [1,2,3] means thread A calls first(), thread B calls second(), and thread C calls third(). "firstsecondthird" is the correct output.

Example 2:
Input: nums = [1,3,2]
Output: "firstsecondthird"
Explanation: The input [1,3,2] means thread A calls first(), thread B calls third(), and thread C calls second(). "firstsecondthird" is the correct output.

Constraints:
nums is a permutation of [1, 2, 3].
"""

# Runtime 46 ms Beats 75.41%
# Memory 17.20 MB Beats 21.62%

import threading
from collections.abc import Callable
class Foo:
    def __init__(self):
        self.event1 = threading.Event()
        self.event2 = threading.Event()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.event1.set()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.event1.wait()
        printSecond()
        self.event2.set()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.event2.wait()
        printThird()

# Runtime 1596 ms Beats 17.43%
# Memory 11.64 MB Beats 77.06%
class Foo2(object):
    def __init__(self):
        self.first_done = False
        self.second_done = False

    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """

        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.first_done = True

    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """
        while not self.first_done: continue
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.second_done = True

    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        while not self.second_done: continue
        # printThird() outputs "third". Do not change or remove this line.
        printThird()

