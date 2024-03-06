def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    if (s == ""): return 0;
    maxx = 1
    llen = len(s)
    for i, ss in enumerate(s):
        s2 = ss
        print(s2,i)
        for j in range(i + 1, llen):
            # print(' ',j,s2,s[j], s[j] not in s2)
            if (s[j] not in s2):
                s2 = s2 + s[j]
                # print('     ',j,'s2 =        ',s2)
                cmax = len(s2)
                if cmax > maxx:
                    maxx = cmax
                    # s3 = s2
            else:
                break
    return maxx

# llst = ["abcabcbb", "bbbbb",  "pwwkew"]
llst = ['au']
for s in llst:
    print(s)
    print('    ',lengthOfLongestSubstring(s))