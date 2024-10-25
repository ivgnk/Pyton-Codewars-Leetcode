"""
25.10.2024. Topics: String, Backtracking
93. Restore IP Addresses
https://leetcode.com/problems/restore-ip-addresses/description

A valid IP address consists of exactly four integers separated by single dots.
Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.
For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses,
but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
Given a string s containing only digits, return all possible valid IP addresses
that can be formed by inserting dots into s.
You are not allowed to reorder or remove any digits in s.
You may return the valid IP addresses in any order.

Example 1:
Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]

Example 2:
Input: s = "0000"
Output: ["0.0.0.0"]

Example 3:
Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

based on https://leetcode.com/problems/restore-ip-addresses/solutions/3079724/backtracking-for-beginners-c-java-js-py-easy-code-explanation-easy-to-understand/
"""

# Runtime 3 ms Beats 98.54%
# Memory 11.64 MB Beats 77.15%
def restoreIpAddresses(s):
    """
    :type s: str
    :rtype: List[str]
    """
    def valid(s):
        if len(s)==0: return False
        elif len(s)>1 and s[0]=='0': return False
        else: return int(s) in range(256)

    ll=len(s)
    if ll == 4: return ['.'.join(list(s))]
    elif ll>12: return []

    res=[]
    for d1 in range(1,4):
        p1=s[0:d1]
        if valid(p1):
            for d2 in range(d1+1,d1+4):
                p2=s[d1:d2]
                if valid(p2):
                    for d3 in range(d2 + 1, d2 + 4):
                        p3=s[d2:d3]
                        p4=s[d3:]
                        if valid(p3) and valid(p4):
                            res.append('.'.join([p1,p2,p3,p4]))

    return res

print(restoreIpAddresses("0000"))
print(restoreIpAddresses("25525511135"))
print(restoreIpAddresses("101023"))