"""
25.09.2024. Topics: Bit Manipulation
190. Reverse Bits
https://leetcode.com/problems/reverse-bits/description/

Reverse bits of a given 32 bits unsigned integer.
Note:

Note that in some languages, such as Java, there is no unsigned integer type.
In this case, both input and output will be given as a signed integer type.
They should not affect your implementation, as the integer's internal binary representation is the same,
whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation.
Therefore, in Example 2 above, the input represents the signed integer -3 and
the output represents the signed integer -1073741825.

Example 1:
Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
Explanation: The input binary string 00000010100101000001111010011100
represents the unsigned integer 43261596,
so return 964176192 which its binary representation is 00111001011110000010100101000000.
Example 2:

Input: n = 11111111111111111111111111111101
Output:   3221225471 (10111111111111111111111111111111)
Explanation: The input binary string 11111111111111111111111111111101
represents the unsigned integer 4294967293,
so return 3221225471 which its binary representation is 10111111111111111111111111111111.

Constraints:
The input must be a binary string of length 32

https://en.wikipedia.org/wiki/Two%27s_complement
"""
from icecream import ic
# https://leetcode.com/problems/reverse-bits/submissions/1401549622/description/comments/1576137
# For test in PyCharm !!!!!!
def reverseBits2(n):
    s="{:032}".format(n); ic(s)
    s=s[::-1]; ic(s)  # reverse oder
    return int("{:032}".format(n)[::-1], 2)

# For work in Leetcode !!!!!!!
def reverseBits(n):
    return int("{:032b}".format(n)[::-1], 2)

###########################################
# https://leetcode.com/problems/reverse-bits/solutions/5816194/1-line-python-code-beating-97-74/
def reverseBits100(n):
    return int(bin(n)[2:].zfill(32)[::-1], 2)

# https://leetcode.com/problems/reverse-bits/solutions/5794379/solution/
def reverseBits101(n):
    bs=format(n,'032b')
    rbs=bs[::-1]
    return int(rbs,2)

# https://leetcode.com/problems/reverse-bits/solutions/5787530/beats-99-79/
def reverseBits102(n):
    binary_conv = bin(n)[2:] #0b is sliced
    binary_num = binary_conv.zfill(32) #filled with extra 0's upto 32 if the size is less than 32
    reversed_str = binary_num[::-1]
    return int(reversed_str,2)

# ic(reverseBits2("00000010100101000001111010011100"))
# ic('----------')
ic(reverseBits2("11111111111111111111111111111101"))
print( int('0b' + bin(s)[2:][::-1], 2) )
# print(reverseBits(s))

