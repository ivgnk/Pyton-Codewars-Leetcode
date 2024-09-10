"""
Done 10.09.2024. Topics: String
1694. Reformat Phone Number
https://leetcode.com/problems/reformat-phone-number/description/

You are given a phone number as a string number. number consists of
digits, spaces ' ', and/or dashes '-'.

You would like to reformat the phone number in a certain manner.
Firstly, remove all spaces and dashes.
Then, group the digits from left to right into blocks of length 3 until
there are 4 or fewer digits.

The final digits are then grouped as follows:
2 digits: A single block of length 2.
3 digits: A single block of length 3.
4 digits: Two blocks of length 2 each.
The blocks are then joined by dashes.
Notice that the reformatting process should never produce any blocks of length 1
and produce at most two blocks of length 2.

Return the phone number after formatting.

Example 1:
Input: number = "1-23-45 6"
Output: "123-456"
Explanation: The digits are "123456".
Step 1: There are more than 4 digits, so group the next 3 digits. The 1st block is "123".
Step 2: There are 3 digits remaining, so put them in a single block of length 3. The 2nd block is "456".
Joining the blocks gives "123-456".

Example 2:
Input: number = "123 4-567"
Output: "123-45-67"
Explanation: The digits are "1234567".
Step 1: There are more than 4 digits, so group the next 3 digits. The 1st block is "123".
Step 2: There are 4 digits left, so split them into two blocks of length 2. The blocks are "45" and "67".
Joining the blocks gives "123-45-67".

Example 3:
Input: number = "123 4-5678"
Output: "123-456-78"
Explanation: The digits are "12345678".
Step 1: The 1st block is "123".
Step 2: The 2nd block is "456".
Step 3: There are 2 digits left, so put them in a single block of length 2. The 3rd block is "78".
Joining the blocks gives "123-456-78".

Constraints:
2 <= number.length <= 100
number consists of digits and the characters '-' and ' '.
There are at least two digits in number.

Hint 1
Discard all the spaces and dashes.
Hint 2
Use a while loop. While the string still has digits, check its length
and see which rule to apply.
"""

# Runtime 16 ms Beats 56.16%
# Memory 11.60 MB Beats 61.64%

def reformatNumber(number):
    """
    :type number: str
    :rtype: str
    """
    s=number.replace('-','').replace(' ','')
    ll=len(s)
    if ll<=3: return s
    elif ll==4: return s[:2]+'-'+s[2:5]
    else:
        n=ll//3
        r=ll%3
        sn=''
        if r==0 or r==2:
            for i in range(n):
                sn+=s[i*3:i*3+3]+'-'
            if r==0: sn=sn[:-1]
            else: sn=sn+s[-2:]
        elif r==1:
            for i in range(n-1):
                sn+=s[i*3:i*3+3]+'-'
            sn = sn+s[-4:-2]+'-'+s[-2:]
    return sn

print(reformatNumber("1-23-45 6"))
print(reformatNumber("1-23-45 67"))
print(reformatNumber("1-23-45 678"))
# print(reformatNumber("1234"))
