"""
Done 28.09.2028. Topics: Queue
641. Design Circular Deque
https://leetcode.com/problems/design-circular-deque/description/

Design your implementation of the circular double-ended queue (deque).

Implement the MyCircularDeque class:

MyCircularDeque(int k) Initializes the deque with a maximum size of k.

boolean insertFront() Adds an item at the front of Deque.
Returns true if the operation is successful, or false otherwise.

boolean insertLast() Adds an item at the rear of Deque.
Returns true if the operation is successful, or false otherwise.

boolean deleteFront() Deletes an item from the front of Deque.
Returns true if the operation is successful, or false otherwise.

boolean deleteLast() Deletes an item from the rear of Deque.
Returns true if the operation is successful, or false otherwise.

int getFront() Returns the front item from the Deque.
Returns -1 if the deque is empty.

int getRear() Returns the last item from Deque.
Returns -1 if the deque is empty.

boolean isEmpty() Returns true if the deque is empty, or false otherwise.

boolean isFull() Returns true if the deque is full, or false otherwise.

Example 1:
Input
["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull", "deleteLast", "insertFront", "getFront"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
[null, true, true, true, false, 2, true, true, true, 4]

Explanation
MyCircularDeque myCircularDeque = new MyCircularDeque(3);
myCircularDeque.insertLast(1);  // return True
myCircularDeque.insertLast(2);  // return True
myCircularDeque.insertFront(3); // return True
myCircularDeque.insertFront(4); // return False, the queue is full.
myCircularDeque.getRear();      // return 2
myCircularDeque.isFull();       // return True
myCircularDeque.deleteLast();   // return True
myCircularDeque.insertFront(4); // return True
myCircularDeque.getFront();     // return 4

Constraints:
1 <= k <= 1000
0 <= value <= 1000
At most 2000 calls will be made to insertFront, insertLast, deleteFront, deleteLast, getFront, getRear, isEmpty, isFull.

Solution
✏ Easy Python solution with "from collections import deque"

Intuition
Geeks program from scratch -
https://www.geeksforgeeks.org/implementation-deque-using-circular-array/
Other people use "from collections import deque" and
don't worry about calculating indices correctly

Approach
Standard Python deque


"""
# Runtime 46 ms Beats 77.78% Analyze Complexity
# Memory 12.16 MB Beats 69.84%
# Time Complexity O(1)
# Space Complexity O(N)

from collections import deque
class MyCircularDeque(object):
    def __init__(self, k):
        """
        :type k: int
        """
        self.list = deque([], k)
        self.currlen = 0
        self.maxlen = k

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.currlen == self.maxlen:
            return False
        else:
            self.list.appendleft(value)
            self.currlen += 1
            return True

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.currlen == self.maxlen:
            return False
        else:
            self.list.append(value)
            self.currlen += 1
            return True

    def deleteFront(self):
        """
        :rtype: bool
        """
        if self.currlen == 0:
            return False
        else:
            self.currlen -=1
            self.list.popleft()
            return True

    def deleteLast(self):
        """
        :rtype: bool
        """
        if self.currlen == 0:
            return False
        else:
            self.currlen -=1
            self.list.pop()
            return True


    def getFront(self):
        """
        :rtype: int
        """
        if self.currlen ==0:
            return -1
        else: return self.list[0]


    def getRear(self):
        """
        :rtype: int
        """
        if self.currlen ==0:
            return -1
        else: return self.list[-1]

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.currlen==0

    def isFull(self):
        """
        :rtype: bool
        """
        return self.currlen==self.maxlen



#####################
# Implementation of Deque using circular array
# https://www.geeksforgeeks.org/implementation-deque-using-circular-array/

# Runtime 50 ms Beats 60.32%
# Memory 12.09 MB Beats 90.48%
# Runtime 47 ms Beats 76.19%
# Memory 12.14 MB Beats 69.84%
# Runtime 46 ms Beats 77.78%
# Memory 12.08 MB Beats 90.48%

class MyCircularDeque2(object):
    def __init__(self, k):
        """
        :type k: int
        """
        self.arr = [0] * k
        self.front = -1
        self.rear = 0
        self.size = k

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        # check whether Deque if  full or not
        if self.isFull():
            # print("Overflow")
            return False

        # If queue is initially empty
        if self.front == -1:
            self.front = 0
            self.rear = 0

        # front is at first position of queue
        elif self.front == 0:
            self.front = self.size - 1

        else:  # decrement front end by '1'
            self.front = self.front - 1

        # insert current element into Deque
        self.arr[self.front] = value
        return True
    # function to inset element at rear end
    # of Deque.

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """

        if self.isFull():
            # print(" Overflow")
            return False

            # If queue is initially empty
        if self.front == -1:
            self.front = 0
            self.rear = 0

            # rear is at last position of queue
        elif (self.rear == self.size - 1):
            self.rear = 0
             # increment rear end by '1'
        else:
            self.rear = self.rear + 1

            # insert current element into Deque
        self.arr[self.rear] = value
        return True

    def deleteFront(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            # print("Queue Underflow")
            return False

        # Deque has only one element
        if (self.front == self.rear):
            self.front = -1
            self.rear = -1
            return True
        else:
            # back to initial position
            if (self.front == self.size - 1):
                self.front = 0

            else:  # increment front by '1' to remove current
                # front value from Deque
                self.front = self.front + 1
            return True

    def deleteLast(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            print(" Underflow")
            return False

        # Deque has only one element
        if (self.front == self.rear):
            self.front = -1
            self.rear = -1
            return True

        elif (self.rear == 0):
            self.rear = self.size - 1
            return True
        else:
            self.rear = self.rear - 1
            return True

    def getFront(self):
        """
        :rtype: int
        """
        if (self.isEmpty()):
            # print(" Underflow")
            return -1

        return self.arr[self.front]

    def getRear(self):
        """
        :rtype: int
        """
        if (self.isEmpty() or self.rear < 0):
            # print(" Underflow")
            return -1

        return self.arr[self.rear]

    def isEmpty(self):
        """
        :rtype: bool
        """
        return (self.front == -1)

    def isFull(self):
        """
        :rtype: bool
        """
        return (self.front == 0 and self.rear == self.size - 1) or self.front == self.rear + 1

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()