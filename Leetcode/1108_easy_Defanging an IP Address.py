'''
1108. Defanging an IP Address
https://leetcode.com/problems/defanging-an-ip-address/description/

Given a valid (IPv4) IP address, return a defanged version of that IP address.
A defanged IP address replaces every period "." with "[.]".

Example 1:
Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"

Example 2:
Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"
'''

# Runtime 15 ms Beats 43.84% of users with Python
# Memory 11.71 MB Beats 24.64% of users with Python

def defangIPaddr(address):
    """
    :type address: str
    :rtype: str
    """
    a = address.replace('.', '[.]')
    return a