'''
Given an integer n, return a string array answer (1-indexed) where:
answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
'''


def fizzBuzz(n):
    """
    :type n: int
    :rtype: List[str]
    """
    llst = [str(i+1) for i in range(n)]
    for i in range(1,n+1):
        if i%3 == 0: llst[i-1] = "Fizz"
        if i%5 == 0: llst[i-1] = "Buzz"
        if (i%3 == 0) and (i%5 == 0): llst[i-1] = "FizzBuzz"
    return llst

print(fizzBuzz(3))