"""
Done 15.10.2024. Topics: Array, Sorting
3169. Count Days Without Meetings
https://leetcode.com/problems/count-days-without-meetings/description/
You are given a positive integer days representing the total number of days an employee
is available for work (starting from day 1).
You are also given a 2D array meetings of size n where, meetings[i] = [start_i, end_i]
represents the starting and ending days of meeting i (inclusive).

Return the count of days when the employee is available for work but no meetings are scheduled.
Note: The meetings may overlap.

Example 1:
Input: days = 10, meetings = [[5,7],[1,3],[9,10]]
Output: 2
Explanation:
There is no meeting scheduled on the 4th and 8th days.

Example 2:
Input: days = 5, meetings = [[2,4],[1,3]]
Output: 1
Explanation:
There is no meeting scheduled on the 5th day.

Example 3:
Input: days = 6, meetings = [[1,6]]
Output: 0
Explanation:
Meetings are scheduled for all working days.

Constraints:
1 <= days <= 109
1 <= meetings.length <= 105
meetings[i].length == 2
1 <= meetings[i][0] <= meetings[i][1] <= days

Hint 1
Merge the overlapping meetings and sort the new meetings timings.
Hint 2
Return the sum of difference between the end time of a meeting and the start time
of the next meeting for all adjacent pairs.

Similar as
# 57. Insert Interval
https://leetcode.com/problems/insert-interval/description/
"""

# Runtime 1259 ms Beats 92.11%
# Memory 65.07 MB Beats 86.84%
class Solution(object):
    def countDays(self, days, meetings):
        """
        :type days: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        #we will simply add all the times in the intervals
        meetings = sorted(meetings, key=lambda x: x[0])
        spent_days  = 0
        start = meetings[0][0]
        end = meetings[0][1]
        for i in meetings[1:]:
            if end >= i[0]:
                end = max(end, i[1])
            else:
                spent_days += end - start + 1
                start = i[0]
                end = i[1]
        spent_days += end - start + 1
        return days -spent_days


# Runtime 8540 ms Beats 5.27%
# Memory 49.28 MB Beats 97.89%
def countDays(days, meetings):
    # sort & merge
    meetings.sort()
    i=1
    while i<len(meetings):
        # print(i,intervals)
        if not meetings[i-1][1]<meetings[i][0]:
            nint=[min(meetings[i-1][0],meetings[i][0]),max(meetings[i-1][1],meetings[i][1])]
            del meetings[i]
            del meetings[i-1]
            meetings.insert(i-1,nint)
        else:
            i+=1
    ss=sum([s[1]-s[0]+1 for s in meetings])
    return days-ss

# print(countDays(days = 10, meetings = [[5,7],[1,3],[9,10]]))
# print(countDays(days = 5, meetings = [[2,4],[1,3]]))
# print(countDays(days = 6, meetings = [[1,6]]))

# Memory Limit Exceeded - 563 / 578 testcases passed
# days = 34384652
# ll=9646 - before merge
# ll=1 - after merge
def countDays3(days, meetings):
    # sort & merge
    meetings.sort()
    i=1
    while i<len(meetings):
        # print(i,intervals)
        if not meetings[i-1][1]<meetings[i][0]:
            nint=[min(meetings[i-1][0],meetings[i][0]),max(meetings[i-1][1],meetings[i][1])]
            del meetings[i]
            del meetings[i-1]
            meetings.insert(i-1,nint)
        else:
            i+=1

    ss = {i for d in meetings for i in range(d[0], d[1] + 1)}
    return days - len(ss)



# Time Limit Exceeded - 562 / 578 testcases passed
# days = 227866
# len(meetings)=873
def countDays2(days, meetings):
    """
    :type days: int
    :type meetings: List[List[int]]
    :rtype: int
    """
    ss = {i for d in meetings for i in range(d[0], d[1] + 1)}
    return days - len(ss)
