"""
Done 03.05.2024
17. Letter Combinations of a Phone Number
https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
Return the answer in any order.
A mapping of digits to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.
"""

# Runtime 7 ms Beats 95.52% of users with Python
# Memory 11.68 MB Beats 74.27% of users with Python

def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    dd={'2': ['a','b','c'], '3': ['d','e','f'], '4': ['g','h','i'], '5': ['j','k','l'], '6': ['m','n','o'],
        '7': ['p','q','r','s'],'8': ['t','u','v'],'9': ['w','x','y','z']}
    ll=len(digits)
    if ll==0: return []
    elif ll==1: return dd[digits]
    else:
        prev=dd[digits[0]]
        for i in range(1,ll):
            res=[]
            arr=dd[digits[i]]
            for w in prev:
                for a in arr:
                    res.append(w+a)
            prev=res
        return prev
print(letterCombinations('23'))
print(letterCombinations('2'))