"""
Done 23.10.2024. Topics: String
468. Validate IP Address
https://leetcode.com/problems/validate-ip-address/solutions/5957013/easy-and-fast-0-ms-python-solution-for-problem-0468/

Given a string queryIP, return "IPv4" if IP is a valid IPv4 address,
"IPv6" if IP is a valid IPv6 address or "Neither" if IP is not a correct IP of any type.

A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 0 <= xi <= 255 and
xi cannot contain leading zeros.
For example, "192.168.1.1" and "192.168.1.0" are valid IPv4 addresses
while "192.168.01.1", "192.168.1.00", and "192.168@1.1" are invalid IPv4 addresses.

A valid IPv6 address is an IP in the form "x1:x2:x3:x4:x5:x6:x7:x8" where:
1 <= xi.length <= 4
xi is a hexadecimal string which may contain digits, lowercase English letter ('a' to 'f')
and upper-case English letters ('A' to 'F').
Leading zeros are allowed in xi.
For example, "2001:0db8:85a3:0000:0000:8a2e:0370:7334" and "2001:db8:85a3:0:0:8A2E:0370:7334" are
valid IPv6 addresses, while "2001:0db8:85a3::8A2E:037j:7334" and "02001:0db8:85a3:0000:0000:8a2e:0370:7334"
are invalid IPv6 addresses.

Example 1:
Input: queryIP = "172.16.254.1"
Output: "IPv4"
Explanation: This is a valid IPv4 address, return "IPv4".

Example 2:
Input: queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
Output: "IPv6"
Explanation: This is a valid IPv6 address, return "IPv6".

Example 3:
Input: queryIP = "256.256.256.256"
Output: "Neither"
Explanation: This is neither a IPv4 address nor a IPv6 address.

My solution
✏️ Easy and fast (0 ms) Python solution for Problem 0468
"""

tr_s=['a','b','c','d','e','f','A','B','C','D','E','F','0','1','2','3','4','5','6','7','8','9']

# Runtime 0 ms Beats 100.00%
# Memory 16.66 MB Beats 33.26%

def validIPAddress(queryIP):
    """
    :type queryIP: str
    :rtype: str
    """
    if '.' in queryIP and ':' in queryIP:
        # print('---')
        return "Neither"
    if '.' in queryIP:
        spl=queryIP.split('.')
        if len(spl)!=4: return "Neither"
        for s in spl:
            try: i=int(s)
            except: return "Neither"
            if i<0 or i>255: return "Neither"
            if len(s)>1 and s[0]=='0': return "Neither"
        return "IPv4"
    elif ':' in queryIP:
        spl = queryIP.split(':')
        if len(spl)!=8: return "Neither"
        for s in spl:
            ll=len(s)
            if ll==0 or ll>4: return "Neither"
            if not all([s1 in tr_s  for s1 in s]): return "Neither"
        return "IPv6"
    else: return "Neither"

print(validIPAddress("12.12.12.12.12"))