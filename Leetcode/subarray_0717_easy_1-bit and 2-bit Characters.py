"""
Done 07.10.2024. Topics: Array
717. 1-bit and 2-bit Characters
https://leetcode.com/problems/1-bit-and-2-bit-characters/

We have two special characters:
The first character can be represented by one bit 0.
The second character can be represented by two bits (10 or 11).
Given a binary array bits that ends with 0, return true if the last
character must be a one-bit character.

Example 1:
Input: bits = [1,0,0]
Output: true
Explanation: The only way to decode it is two-bit character and one-bit character.
So the last character is one-bit character.

Example 2:
Input: bits = [1,1,1,0]
Output: false
Explanation: The only way to decode it is two-bit character and two-bit character.
So the last character is not one-bit character.

Constraints:
1 <= bits.length <= 1000
bits[i] is either 0 or 1.

Hint 1
Keep track of where the next character starts.
At the end, you want to know if you started on the last bit.

Main tips in discussion
https://leetcode.com/problems/1-bit-and-2-bit-characters/description/comments/2225553
https://leetcode.com/problems/1-bit-and-2-bit-characters/description/comments/1866786
https://leetcode.com/problems/1-bit-and-2-bit-characters/description/comments/2550440

My solution
https://leetcode.com/problems/1-bit-and-2-bit-characters/solutions/5882667/python-solution-with-simulating-process/
"""

# Runtime 30 ms Beats 68.10%
# Memory 11.71 MB Beats 23.31%
def isOneBitCharacter(bits):
    ll = len(bits)
    if bits.count(0)==ll: return True
    if ll == 1: return bits == [0]
    if ll <= 2: return bits == [0, 0]
    if ll == 3: return bits == [0, 0, 0] or bits == [1, 0, 0] or bits == [1, 1, 0]
    i=0
    while i<ll-1:
        if bits[i]==0: i+=1
        else: i+=2
    print(i)
    if i==ll-1:  return bits[i]==0

    else: return False

# print(isOneBitCharacter([1,0,0]))
# print(isOneBitCharacter([1,1,1,0]))
print(isOneBitCharacter([0,0,0,0]))



tr=['0000', '0100', '0110', '1000', '1100']
def isOneBitCharacter2(bits):
    """
    :type bits: List[int]
    :rtype: bool
    """
    ll = len(bits)
    if ll == 1: return bits == [0]
    if ll <= 2: return bits == [0, 0]
    if ll == 3: return bits == [0, 0, 0] or bits == [1, 0, 0] or bits == [1, 1, 0]
    else:
        s=''.join(map(str,bits[-4:]))
        return s in tr

