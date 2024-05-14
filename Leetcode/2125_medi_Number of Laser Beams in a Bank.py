"""
Done 14.05.2024. Topics: Array, Math, String, Matrix

2125. Number of Laser Beams in a Bank
https://leetcode.com/problems/number-of-laser-beams-in-a-bank/description/

Anti-theft security devices are activated inside a bank. You are given a 0-indexed binary string array bank representing the floor plan of the bank, which is an m x n 2D matrix. bank[i] represents the ith row, consisting of '0's and '1's. '0' means the cell is empty, while'1' means the cell has a security device.

There is one laser beam between any two security devices if both conditions are met:

The two devices are located on two different rows: r1 and r2, where r1 < r2.
For each row i where r1 < i < r2, there are no security devices in the ith row.
Laser beams are independent, i.e., one beam does not interfere nor join with another.

Return the total number of laser beams in the bank.

Example 1:
Input: bank = ["011001","000000","010100","001000"]
Output: 8
Explanation: Between each of the following device pairs, there is one beam. In total, there are 8 beams:
 * bank[0][1] -- bank[2][1]
 * bank[0][1] -- bank[2][3]
 * bank[0][2] -- bank[2][1]
 * bank[0][2] -- bank[2][3]
 * bank[0][5] -- bank[2][1]
 * bank[0][5] -- bank[2][3]
 * bank[2][1] -- bank[3][2]
 * bank[2][3] -- bank[3][2]
Note that there is no beam between any device on the 0th row with any on the 3rd row.
This is because the 2nd row contains security devices, which breaks the second condition.

Example 2:
Input: bank = ["000","111","000"]
Output: 0
Explanation: There does not exist two devices located on two different rows.
"""

# Runtime 72 ms Beats 69.31% of users with Python
# Memory 14.96 MB Beats 99.50% of users with Python
# Runtime 65 ms Beats 92.08%# of users with Python
# Memory 15.27 MB Beats# 56.44% of users with Python

def numberOfBeams2(bank):
    """
    :type bank: List[str]
    :rtype: int
    """
    b2=[s for s in bank if '1' in s]
    ssum=0
    for i in range(1,len(b2)):
        ssum=ssum+b2[i-1].count('1')*b2[i].count('1')
    return ssum

# Runtime 59 ms Beats 96.53% of users with Python
# Memory 15.26 MB Beats 56.44% of users with Python
def numberOfBeams(bank):
    """
    :type bank: List[str]
    :rtype: int
    """
    b2=[s for s in bank if '1' in s]
    return sum(b2[i-1].count('1')*b2[i].count('1') for i in range(1,len(b2)))

print(numberOfBeams(["011001","000000","010100","001000"]))

