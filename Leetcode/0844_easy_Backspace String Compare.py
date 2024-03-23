'''
Given two strings s and t, return true if they are equal when both are typed into empty text editors.
'#' means a backspace character.
Note that after backspacing an empty text, the text will continue empty.

Example 1:
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Example 2:
Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

Example 3:
Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
'''

# Runtime 12 ms
# Beats # 78.56% of users with Python
# Memory 11.72MB
# Beats 23.49% of users with Python


def backspaceCompare(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """

    def delleads(s):
        si_s = s.find('#')
        while si_s == 0:
            s = s[1:]
            si_s = s.find('#')
        return s

    si_s = s.find('#')
    si_t = t.find('#')
    if s=='' and t=='': return True

    s = delleads(s)
    si_s = s.find('#')
    while si_s>-1:
        while si_s>0:
            s = s[:si_s-1] + s[si_s+1:]
            si_s = s.find('#')
        s = delleads(s)
        si_s = s.find('#')

    t = delleads(t)
    si_t = t.find('#')
    while si_t>-1:
        while si_t>0:
            t =  t[:si_t-1] + t[si_t+1:]
            si_t = t.find('#')
        t = delleads(t)
        si_t = t.find('#')
    print(f'{s=}  {t=}')
    return t==s

print(backspaceCompare(s = "ab#c", t = "ad#c")) # True
# print(backspaceCompare("c##vnvr","c##vn#nvr"))
#     print(f'{s=}  {t=}')