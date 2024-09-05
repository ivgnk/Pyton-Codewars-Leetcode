"""
05.09.2024. Topics: Array, Stack
155. Min Stack
https://leetcode.com/problems/min-stack/description/

Design a stack that supports push, pop, top, and retrieving the
minimum element in constant time.

Implement the MinStack class:
MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

Constraints:
-2**31 <= val <= 2**31 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 10**4 calls will be made to push, pop, top, and getMin.

Hint 1
Consider each node in the stack having a minimum value. (Credits to
"""
# Runtime 47 ms Beats 91.00%
# Memory 20.75 MB Beats 24.17%

# https://leetcode.com/problems/min-stack/solutions/5738137/min-stack-solution-beats-96-73-of-users-in-runtime/
class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        min_so_far = min(val, self.stack[-1][1]) if self.stack else val
        self.stack.append((val, min_so_far))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

