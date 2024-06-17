"""
Done 17.06.2024. Topics: String
551. Student Attendance Record I
https://leetcode.com/problems/student-attendance-record-i/description/

You are given a string s representing an attendance record for a student where each character signifies
whether the student was absent, late, or present on that day. The record only contains the following three characters:

'A': Absent.
'L': Late.
'P': Present.
The student is eligible for an attendance award if they meet both of the following criteria:

The student was absent ('A') for strictly fewer than 2 days total.
The student was never late ('L') for 3 or more consecutive days.
Return true if the student is eligible for an attendance award, or false otherwise.

Example 1:
Input: s = "PPALLP"
Output: true
Explanation: The student has fewer than 2 absences and was never late 3 or more consecutive days.

Example 2:
Input: s = "PPALLL"
Output: false
Explanation: The student was late 3 consecutive days in the last 3 days, so is not eligible for the award.
"""

# Runtime 10 ms Beats 84.41% - Time Complexity O(N)
# Memory 11.69 MB Beats 52.48% - Space Complexity O(1)

def checkRecord(s):
    """
    :type s: str
    :rtype: bool
    """
    if s.count('A')>=2: return False
    elif s.find('LLL')>-1: return False
    return True
