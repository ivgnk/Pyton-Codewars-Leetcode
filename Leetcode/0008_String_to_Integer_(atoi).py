'''
    https://leetcode.com/problems/string-to-integer-atoi/?source=submission-noac
    Не закончено
'''
def myAtoi(s):
    """
    :type s: str
    :rtype: int
    """
    s2 = str(s)
    s2 = str.strip(s2)
    if len(s2) == 0: return 0
    if (s2 == "+") or (s2 == "-"): return 0
    if s2[0].isalpha(): return 0;
    # if s2.find('.') != -1: return 0
    s2 = ''.join(i for i in s2 if not i.isalpha())
    if s2.find('+-') != -1: return 0
    if s2.find('-+') != -1: return 0
    # s2 = s2.replace("+-",'')
    # s2 = s2.replace("-+",'-')

    if s2.find('.') == -1:
        rr = int(s2)
    else:
        rr = int(float(s2))
    if rr <= -2147483648: return -2147483648
    if rr >= 2147483647: return 2147483647
    return rr


print(myAtoi("-4193 with words"))
print(myAtoi("words and 987"))
print(myAtoi("3.14159"))
print(myAtoi("00000-42a1234"))

