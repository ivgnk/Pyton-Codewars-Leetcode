def isSubsequence( s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if t.find(s) >= 0: return True
    sets = set(s)
    sett = set(t)
    sr = sett - sets;    print(sr)
    tlist = list(t);    slist = list(s)
    tnew = []
    for i, ss in enumerate(tlist):
        if not (ss in sr):
            tnew.append(ss)
    print(tnew);    print(slist)
    return tnew == slist