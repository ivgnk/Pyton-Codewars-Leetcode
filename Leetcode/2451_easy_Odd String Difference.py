'''
2451. Odd String Difference
https://leetcode.com/problems/odd-string-difference/


'''


def oddString(self, words):
    """
    :type words: List[str]
    :rtype: str
    """
    llenw = len(words[0])
    diff = [0] * (llenw - 1)
    arrdiff = []
    for ss in words:
        for j, sss in enumerate(ss):
            if j <= llenw - 1:
                print(j)
                diff[j] = ord(ss[j + 1]) - ord(ss[j])
        arrdiff.append(diff)
    print(arrdiff)
    return None
