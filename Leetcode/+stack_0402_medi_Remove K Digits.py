"""
17.04.2024. Topics: Monotonic Stack
402. Remove K Digits
Given string num representing a non-negative integer num, and an integer k,
return the smallest possible integer after removing k digits from num.

Example 1:
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2
to form the new number 1219 which is the smallest.

Example 2:
Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200.
Note that the output must not contain leading zeroes.

Example 3:
Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.

Constraints:
1 <= k <= num.length <= 105
num consists of only digits.
num does not have any leading zeros except for the zero itself.
"""
from icecream import ic

def removeKdigits2(num, k):
    """
    :type num: str
    :type k: int
    :rtype: str
    """
    ll=len(num)
    llmk=ll-k
    lst=list(num)
    i=0
    while i<len(lst)-1:
        if lst[i]>lst[i+1]:
            del lst[i]
        i=i+1
    if len(lst) == llmk:
        print('1')
        return ''.join(lst)
    i=0
    while i<len(lst)-1:
        if lst[i]>lst[i+1]:
            del lst[i]
        i=i+1
    return ''.join(lst)

def removeKdigits3(num, k):
    ans=""; ll=len(num)
    if k==2 and num==2: return 0
    for ik in range(k):
        for i in range(ll-1):
            if num[i]<num[i+1]:
                ans+=num[i]
            else:
                if num[i]>num[i+1]:
                    continue
    return ans

# Wrong Answer - 32 / 43 testcases passed
def removeKdigits4(num, k):
    if len(num) == k: return "0"
    if len(num) - 1 == k and '0' in num: return "0"
    stck=[]
    for s in num:
        if stck and k>0:
            if s<stck[-1]:
                stck.pop()
                k-=1
        stck.append(s)
    for i in range(k): stck.pop()
    if stck[0] == '0':
        if len(stck) == 1: return "0"
        else:
            print(stck)
            while stck and stck[0]=='0':
                del stck[0]
            print(stck)

    # ic(k,stck)
    if stck == []: return "0"
    else: return ''.join(stck)

# Runtime 16 ms Beats 100.00%
# Memory 13.04 MB Beats 84.03%
# https://leetcode.com/problems/remove-k-digits/solutions/5876960/python-easy-beats-99/
def removeKdigits(num: str, k: int) -> str:
    stack = []
    if k == len(num): return "0"

    for digit in num:
        while k > 0 and stack and digit < stack[-1]:
            stack.pop()
            k -= 1
        stack.append(digit)

    stack = stack[:len(stack) - k]
    return ''.join(stack).lstrip('0') or "0"

# ic(removeKdigits(num = "1432219", k = 3))
# ic(removeKdigits("10200", 1))
ic(removeKdigits("100", 1))
# ic(removeKdigits("10", 2))
# ic(removeKdigits("10001", 1))
# ic(removeKdigits("112", 1))


def monot_decrasing_stack():
    dat=[0, 2, 1, 3, 4]
    ll=len(dat)
    result = [None]*ll
    stack = []  # invariant: stack is decreasing
    for i in dat:
        while stack and i > stack[-1]:
            result[stack.pop()] = i
        stack.append(i)
    return result

def monot_decrasing_stack2():
    # dat=[0, 2, 1, 3, 4]
    dat=[2, 1, 2, 4, 3]
    stack = []  # invariant: stack is decreasing
    for i in dat:
        while stack and i > stack[-1]:
            stack.pop()
        stack.append(i)
    return stack

# print(monot_decrasing_stack2())

# https://www.geeksforgeeks.org/monotonic-stack-in-python/
def monotonic_decreasing_stack(arr):
    # Initialize an empty stack to maintain the decreasing order
    stack = []
    # Iterate through each element in the input array
    for num in arr:
        # While the stack is not empty and the top of the stack is less than the current element
        while stack and stack[-1] < num:
            # Pop the top element from the stack
            stack.pop()
        # Push the current element onto the stack
        stack.append(num)

    # Return the stack, which now contains elements in monotonic decreasing order
    return stack

# https://www.geeksforgeeks.org/monotonic-stack-in-python/
def monotonic_increasing_stack(arr):
    # Initialize an empty stack to maintain the increasing order
    stack = []

    # Iterate through each element in the input array
    for num in arr:
        # While the stack is not empty and the top of the stack is greater than the current element
        while stack and stack[-1] > num:
            # Pop the top element from the stack
            stack.pop()
        # Push the current element onto the stack
        stack.append(num)

    # Return the stack, which now contains elements in monotonic increasing order
    return stack


# Example usage
# arr = [2, 1, 2, 4, 3]
# arr="10200"
# ic(monotonic_decreasing_stack(arr))
# ic(monotonic_increasing_stack(arr))

# # ic(monot_decrasing_stack())
# ic(monotonic_decreasing_stack("1432219"))