"""
Done 05.09.2024. Topics: Array, Stack
150. Evaluate Reverse Polish Notation
You are given an array of strings tokens that represents
an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:
The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.


Example 1:
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

Constraints:
1 <= tokens.length <= 10**4
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].

Runtime 61 ms Beats 81.63%
Memory 17.01 MB Beats 61.26%

Solution
✏️ Easy Python solution with two nuances

# Intuition
Use stack

# Approach
Two nuances:
1) result push into stack
2) do not forget to convert to an integer

"""
def oper(f,op,l):
    if type(f)!=int: f=int(f)
    if type(l)!=int: l=int(l)
    match op:
        case '+': return f+l
        case '-': return f-l
        case '*': return f*l
        case '/': return f/l

def evalRPN(tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """
    ll = len(tokens)
    if ll == 1: return int(tokens[0])

    stck = []; res = None
    for d in tokens:
        if d.isnumeric() or d[1:].isnumeric():
            stck.append(int(d))
        elif res is None:
            two = stck.pop()
            res = stck.pop()
            res = oper(res, d, two)
            stck.append(res)
        else:
            two = stck.pop()
            res = stck.pop()
            res = oper(res, d, two)
            stck.append(res)
    return int(res)

# print(evalRPN(["2","1","+","3","*"]))
# print(evalRPN(["4","13","5","/","+"]))
print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
