"""
17.12.2024. Topics: Hash Table, Heap (Priority Queue)
2182. Construct String With Repeat Limit
https://leetcode.com/problems/construct-string-with-repeat-limit/

You are given a string s and an integer repeatLimit.
Construct a new string repeatLimitedString using the characters of s such that no letter
appears more than repeatLimit times in a row. You do not have to use all characters from s.

Return the lexicographically largest repeatLimitedString possible.

A string a is lexicographically larger than a string b if in the first position where a and b differ,
string a has a letter that appears later in the alphabet than the corresponding letter in b.
If the first min(a.length, b.length) characters do not differ, then the longer string is the
lexicographically larger one.

Example 1:
Input: s = "cczazcc", repeatLimit = 3
Output: "zzcccac"
Explanation: We use all of the characters from s to construct the repeatLimitedString "zzcccac".
The letter 'a' appears at most 1 time in a row.
The letter 'c' appears at most 3 times in a row.
The letter 'z' appears at most 2 times in a row.
Hence, no letter appears more than repeatLimit times in a row and the string is a valid repeatLimitedString.
The string is the lexicographically largest repeatLimitedString possible so we return "zzcccac".
Note that the string "zzcccca" is lexicographically larger but the letter 'c' appears more than 3 times in a row, so it is not a valid repeatLimitedString.

Example 2:
Input: s = "aababab", repeatLimit = 2
Output: "bbabaa"
Explanation: We use only some of the characters from s to construct the repeatLimitedString "bbabaa".
The letter 'a' appears at most 2 times in a row.
The letter 'b' appears at most 2 times in a row.
Hence, no letter appears more than repeatLimit times in a row and the string is a valid repeatLimitedString.
The string is the lexicographically largest repeatLimitedString possible so we return "bbabaa".
Note that the string "bbabaaa" is lexicographically larger but the letter 'a' appears more than 2 times in a row, so it is not a valid repeatLimitedString.

Constraints:
1 <= repeatLimit <= s.length <= 105
s consists of lowercase English letters.

Hint 1
Start constructing the string in descending order of characters.
Hint 2
When repeatLimit is reached, pick the next largest character.
"""
from collections import Counter, OrderedDict

# Runtime 319 ms Beats 27.18%
# Memory 19.75 MB Beats 8.74%
def repeatLimitedString(s, repeatLimit):
    """
    :type s: str
    :type repeatLimit: int
    :rtype: str
    """
    # dd=dict()
    # for s1 in s:
    #     if s1 in dd:
    #         dd[s1]+=1
    #     else:
    #         dd[s1] = 1
    # lst=sorted([(k,v) for k,v in dd.items()], reverse=True)
    # for s
    lst = sorted(list(s), reverse=True)
    cnt = 1
    j=0
    for i in range(1, len(lst)):
        if lst[i-1] == lst[i]:
            cnt+=1
            if cnt > repeatLimit:
                j=max(j, i+1)
                while j<len(lst):
                    if lst[j] != lst[i]:
                        lst[j], lst[i] = lst[i], lst[j]
                        cnt=1
                        break
                    j+=1
                if j>=len(lst):
                    return ''.join(lst[:i])
        else:
          cnt = 1
    return ''.join(lst)

class Solution2:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        hmap = OrderedDict(Counter(s))
        hmap = dict(sorted(hmap.items(), key=lambda x: x[0], reverse=True))
        result = ""

        while len(hmap) > 0:
            keys = list(hmap.keys())
            first = keys[0]

            if hmap[first] > repeatLimit:
                result += first * repeatLimit
                hmap[first] -= repeatLimit
                if len(hmap) == 1:
                    return result
                result += keys[1]
                hmap[keys[1]] -= 1

                if hmap[keys[1]] == 0:
                    del hmap[keys[1]]
            else:
                result += first * hmap[first]
                del hmap[first]
        return result

class Solution3:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        table = Counter(s)
        char_set = ['0', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                    'r', 's',
                    't', 'u', 'v', 'w', 'x', 'y', 'z']
        sorted_table = []
        for i in range(26, -1, -1):
            if char_set[i] in table:
                sorted_table.append((char_set[i], table[char_set[i]]))

        result = ""
        n = len(sorted_table)
        for i in range(n):
            char, curr_freq = sorted_table[i]  # The lexicographically larger character and its frequency
            index_to_take_from = i + 1  # We take from this index the next lexicographically larger character(TEMP) if the repeatLimit for A is exceeded
            while curr_freq > repeatLimit:  # Limit exceeded
                result += char * repeatLimit  # Add repeatLimit number of character A's
                curr_freq -= repeatLimit  # Decrease frequency of character A
                # Now we search for the next lexicographically superior character that can be used once
                while index_to_take_from < n:  # Till we run out of characters
                    ch_avail, freq_avail = sorted_table[index_to_take_from]
                    if freq_avail == 0:  # If its freq is 0 that means that it was previously used. This is done as we are not removing the character from table if its freq becomes 0.
                        index_to_take_from += 1  # Check for next lexicographically superior character
                    else:
                        result += ch_avail  # If found then add that character
                        sorted_table[index_to_take_from] = (
                        ch_avail, freq_avail - 1)  # Update the new characters frequency
                        break
                else:
                    break  # We cannot find any lexicographically superior character
            else:
                result += char * curr_freq  # If the freq is in limits then just add them
        return result


import heapq
from heapq import heappop, heappush

class Solution4:
    def repeatLimitedString(self, s: str, r: int) -> str:
        cnt = Counter(s)

        q = [-(ord(x) - ord('a')) for x in cnt]
        heapq.heapify(q)

        wait = ''
        ans = ''
        while q:

            cur = chr(ord('a') - heappop(q))
            if wait:
                ans += cur
                cnt[cur] -= 1
                if cnt[cur]:
                    heappush(q, -(ord(cur) - ord('a')))
                heappush(q, -(ord(wait) - ord('a')))
                wait = ""
            else:
                if cnt[cur] <= r:
                    ans += cur * cnt[cur]
                else:
                    ans += cur * r
                    cnt[cur] -= r
                    wait = cur

        return ans


# https://leetcode.com/problems/construct-string-with-repeat-limit/submissions/1480746900/
class Solution5:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        chars = Counter(s)
        sorted_chars = sorted(chars.items(), reverse=True)

        ans = []

        while sorted_chars:
            char, freq = sorted_chars[0]
            if freq <= repeatLimit:
                ans.append(char * freq)
                sorted_chars.pop(0)
            else:
                ans.append(char * repeatLimit)
                sorted_chars[0] = (char, freq - repeatLimit)

                if len(sorted_chars) > 1:
                    next_char, next_freq = sorted_chars[1]
                    ans.append(next_char)
                    if next_freq == 1:
                        sorted_chars.pop(1)
                    else:
                        sorted_chars[1] = (next_char, next_freq - 1)
                else:
                    break

        return ''.join(ans)

import collections
# https://leetcode.com/problems/construct-string-with-repeat-limit/solutions/1939671/python-solution-faster-than-99-python-su-qggw/
def repeatLimitedString(s: str, k: int) -> str:
    arr = sorted([[a, b] for a, b in collections.Counter(s).items()], key=lambda x: x[0], reverse=True)
    i, j, n = 0, 1, len(arr)
    ans = ''
    while j < n:
        if arr[i][1] > k:
            ans += arr[i][0] * k + arr[j][0]
            arr[i][1] -= k
            arr[j][1] -= 1
            if arr[j][1] == 0: j += 1
        else:
            ans += arr[i][0] * arr[i][1]
            i, j = j, j + 1
    rem = k if arr[i][1] > k else arr[i][1]
    ans += arr[i][0] * rem
    return ans

# https://leetcode.com/problems/construct-string-with-repeat-limit/solutions/1953156/8-lines-python-solution-80-faster-memory-23ke/
class Solution6:
    def repeatLimitedString(self, s: str, l: int) -> str:
        C=[list(x) for x in sorted(Counter(s).items(),reverse=True)] ; ans=''
        if len(C)==1: return C[0][0]*l
        while len(C)>1:
            ans+=C[0][0]*min(C[0][1],l)
            C[0][1]-=min(C[0][1],l)
            if C[0][1]>0: ans+=C[1][0] ; C[1][1]-=1
            C=[c for c in C if c[1]>0]
        return ans+C[0][0]*min(C[0][1],l)

# https://leetcode.com/problems/construct-string-with-repeat-limit/solutions/6154418/for-beginners-heappython-by-jayanth_y-ig6k/
class Solution7:
    def repeatLimitedString(self, s: str, rl: int) -> str:
        h = [ (-ord(x), y) for x, y in Counter(s).items() ]
        heapq.heapify(h)
        res = ""

        while h:
            x, y = heapq.heappop(h)
            while y > rl and h:
                res += chr(-x) * rl
                y -= rl
                a, b = heapq.heappop(h)
                res += chr(-a)
                if (b-1) > 0: heapq.heappush(h, (a, b-1))
            res += chr(-x) * y

        if res:
            i = len(res)-1
            while i >= 0 and res[i] == res[-1]: i -= 1
            if len(res)-i-1 > rl: res = res[:i+1+rl]

        return res