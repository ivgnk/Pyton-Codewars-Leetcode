"""
Done 18.08.2024. Topics: Array, String
2446. Determine if Two Events Have Conflict
https://leetcode.com/problems/determine-if-two-events-have-conflict/description/

You are given two arrays of strings that represent two inclusive events
that happened on the same day, event1 and event2, where:
event1 = [startTime1, endTime1] and
event2 = [startTime2, endTime2].
Event times are valid 24 hours format in the form of HH:MM.
A conflict happens when two events have some non-empty intersection (i.e., some moment is common to both events).
Return true if there is a conflict between two events. Otherwise, return false.

Example 1:
Input: event1 = ["01:15","02:00"], event2 = ["02:00","03:00"]
Output: true
Explanation: The two events intersect at time 2:00.

Example 2:
Input: event1 = ["01:00","02:00"], event2 = ["01:20","03:00"]
Output: true
Explanation: The two events intersect starting from 01:20 to 02:00.

Example 3:
Input: event1 = ["10:00","11:00"], event2 = ["14:00","15:00"]
Output: false
Explanation: The two events do not intersect.

Constraints:
event1.length == event2.length == 2
event1[i].length == event2[i].length == 5
startTime1 <= endTime1
startTime2 <= endTime2
All the event times follow the HH:MM format.

Solution
✏️ Easy Python solution with sorting events
# Intuition
Comparing the time of the end of event 1 and the beginning of event 2

# Approach
Time comparison should be performed for sorted events.
In examples 1-3, the events are sorted, but not always in other tests.
Done 18.08.2024
Runtime 27 ms Beats 94.32%
Memory 16.50 MB Beats 24.29%

"""

# Runtime 36 ms Beats 50.16%
# Memory 16.55 MB Beats 24.29%
# Runtime 27 ms Beats 94.32%
# Memory 16.50 MB Beats 24.29%

from icecream import ic
def haveConflict(event1, event2):
    """
    :type event1: List[str]
    :type event2: List[str]
    :rtype: bool
    """

    e1b=event1[0].split(':')
    e1e=event1[1].split(':')

    e2b=event2[0].split(':')
    e2e=event2[1].split(':')

    p1_beg=int(e1b[0])*60+int(e1b[1])
    p1_end=int(e1e[0])*60+int(e1e[1])

    p2_beg=int(e2b[0])*60+int(e2b[1])
    p2_end=int(e2e[0])*60+int(e2e[1])

    if p2_beg<p1_beg:
        p1_beg, p1_end, p2_beg,  p2_end = p2_beg,  p2_end, p1_beg, p1_end
    return p1_end>=p2_beg

# ic(haveConflict(event1 = ["01:15","02:00"], event2 = ["02:00","03:00"])) #  True
# ic(haveConflict(event1 = ["01:00","02:00"], event2 = ["01:20","03:00"])) #  True
# ic(haveConflict(event1 = ["10:00","11:00"], event2 = ["14:00","15:00"])) #  False
# ic(haveConflict(event1 = ["14:13","22:08"], event2 = ["02:40","08:08"])) #  False


