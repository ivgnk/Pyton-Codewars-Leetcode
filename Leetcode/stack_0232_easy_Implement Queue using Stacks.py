"""
Done 13.08.2024. Topics: Stack, Queue
232. Implement Queue using Stacks
https://leetcode.com/problems/implement-queue-using-stacks/description/

Implement a first in first out (FIFO) queue using only two stacks.
The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:
void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.

Notes:
You must use only standard operations of a stack, which means only
push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively.
You may simulate a stack using a list or deque (double-ended queue)
as long as you use only a stack's standard operations.

Example 1:
Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]
Explanation
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false

Constraints:
1 <= x <= 9
At most 100 calls will be made to push, pop, peek, and empty.
All the calls to pop and peek are valid.

Solution
✏️ Easy Python solution with list

Intuition
Use the list and its built-in functions

Approach
Done 13.08.2024.
Runtime 11 ms Beats 77.65%
Memory 11.69 MB Beats 57.42%

Time Complexity O(1)
Space Complexity O(N)
"""

# Runtime 14 ms Beats 50.76%
# Memory 11.73 MB Beats 23.03%
# Runtime 11 ms Beats 77.65%
# Memory 11.69 MB Beats 57.42%

class MyQueue(object):
    def __init__(self):
        self.dat = []

    def push(self, x):
        self.dat.append(x)

    def pop(self):
        return self.dat.pop(0)

    def peek(self):
        return self.dat[0]

    def empty(self):
        return self.dat == []

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
