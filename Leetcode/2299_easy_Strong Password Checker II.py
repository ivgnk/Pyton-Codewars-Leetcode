"""
23.10.2024. Topics: String
2299. Strong Password Checker II.
https://leetcode.com/problems/strong-password-checker-ii/description

A password is said to be strong if it satisfies all the following criteria:
It has at least 8 characters.
It contains at least one lowercase letter.
It contains at least one uppercase letter.
It contains at least one digit.
It contains at least one special character.
The special characters are the characters in the following string:
"!@#$%^&*()-+".
It does not contain 2 of the same character in adjacent positions
(i.e., "aab" violates this condition, but "aba" does not).
Given a string password, return true if it is a strong password.
Otherwise, return false.


Example 1:
Input: password = "IloveLe3tcode!"
Output: true
Explanation: The password meets all the requirements. Therefore, we return true.

Example 2:
Input: password = "Me+You--IsMyDream"
Output: false
Explanation: The password does not contain a digit and also contains 2 of the same character in adjacent positions. Therefore, we return false.

Example 3:
Input: password = "1aB!"
Output: false
Explanation: The password does not meet the length requirement. Therefore, we return false.

Constraints:
1 <= password.length <= 100
password consists of letters, digits, and special characters: "!@#$%^&*()-+".

Hint 1
You can use a boolean flag to define certain types of characters seen in the string.
Hint 2
In the end, check if all boolean flags have ended up True,
and do not forget to check the "adjacent" and "length" criteria.

My solution https://leetcode.com/problems/strong-password-checker-ii/solutions/5956896/fast-1-ms-and-easy-python-solution-for-problem-2299/
✏️ Fast (1 ms) and easy Python solution for Problem 2299
"""

# Runtime 1 ms Beats 93.85%
# Memory 11.53 MB Beats 73.85%
# Time Complexity O(N)
# Space Complexity O(1)

spc="!@#$%^&*()-+"
def strongPasswordCheckerII(password):
    """
    :type password: str
    :rtype: bool
    """
    ll=len(password)
    if ll<8: return False
    nlow=0; nup=0; ndg=0; nsp=0
    prev=''; notsame=True
    for s in password:
        if s.islower(): nlow+=1
        if s.isupper(): nup+=1
        if s.isdigit(): ndg+=1
        if s in spc: nsp+=1
        notsame=notsame and (prev !=s)
        prev = s
    if nlow<1 or nup<1 or ndg<1 or nsp<1: return False
    if not notsame: return False
    return True



