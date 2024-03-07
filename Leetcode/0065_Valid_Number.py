def isNumber(s):
    """
    :type s: str
    :rtype: bool
    """
    if s.isalpha(): return False
    if 'inf' in s.lower(): return False
    try:
        x = float(s)
    except:
        return False
    return True

