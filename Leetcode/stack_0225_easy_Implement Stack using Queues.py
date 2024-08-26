"""
Done 26.08.2024. Topics: Stack, Queue
225. Implement Stack using Queues
https://leetcode.com/problems/implement-stack-using-queues/description/

Implement a last-in-first-out (LIFO) stack using only two queues.
The implemented stack should support all the functions of a normal stack
(push, top, pop, and empty).

Implement the MyStack class:
void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.

Notes:
You must use only standard operations of a queue, which means that only push to back,
peek/pop from front, size and is empty operations are valid.
Depending on your language, the queue may not be supported natively.
You may simulate a queue using a list or deque (double-ended queue)
as long as you use only a queue's standard operations.

Example 1:
Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 2, 2, false]

Explanation
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False


Constraints:
1 <= x <= 9
At most 100 calls will be made to push, pop, top, and empty.
All the calls to pop and top are valid.

Follow-up: Can you implement the stack using only one queue?
"""

# Runtime 12 ms Beats 70.17%
# Analyze Complexity
# Memory
# 11.82
# MB
# Beats
# 6.74%
# Runtime 3 ms Beats 99.70%
# Memory 11.72 MB Beats 28.94%

class MyStack2(object):

    def __init__(self):
        self.st=[]

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.st.append(x)

    def pop(self):
        """
        :rtype: int
        """
        return self.st.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.st[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.st)==0

# https://docs.python.org/3/library/collections.html#collections.deque
# https://docs-python.ru/standart-library/modul-collections-python/klass-deque-modulja-collections/

# Runtime 7 ms Beats 95.04%
# Memory 11.68 MB Beats 64.69%
from collections import deque

class MyStack(object):

    def __init__(self):
        self.st=deque([])

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.st.append(x)

    def pop(self):
        """
        :rtype: int
        """
        return self.st.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.st[-1]

    def empty(self):
        """
        :rtype: bool
        """
        # return self.st.count()==0 - тоже работает
        return len(self.st) == 0