"""
16.12.2024
3386. Button with Longest Push Time
https://leetcode.com/problems/button-with-longest-push-time/description/

You are given a 2D array events which represents a sequence of events where
a child pushes a series of buttons on a keyboard.

Each events[i] = [indexi, timei] indicates
that the button at index indexi was pressed at time timei.

The array is sorted in increasing order of time.
The time taken to press a button is the difference in time between consecutive button presses.
The time for the first button is simply the time at which it was pressed.
Return the index of the button that took the longest time to push.
If multiple buttons have the same longest time, return the button with the smallest index.

Example 1:
Input: events = [[1,2],[2,5],[3,9],[1,15]]
Output: 1
Explanation:
Button with index 1 is pressed at time 2.
Button with index 2 is pressed at time 5, so it took 5 - 2 = 3 units of time.
Button with index 3 is pressed at time 9, so it took 9 - 5 = 4 units of time.
Button with index 1 is pressed again at time 15, so it took 15 - 9 = 6 units of time.

Example 2:
Input: events = [[10,5],[1,7]]
Output: 10
Explanation:
Button with index 10 is pressed at time 5.
Button with index 1 is pressed at time 7, so it took 7 - 5 = 2 units of time.

Constraints:
1 <= events.length <= 1000
events[i] == [indexi, timei]
1 <= indexi, timei <= 105
The input is generated such that events is sorted in increasing order of timei.
"""

# https://leetcode.com/problems/button-with-longest-push-time/solutions/6150938/beats-100-3ms-python-3/
from typing import List
# Runtime 0 ms Beats 100.00%
# Memory 17.66 MB Beats 100.00%
class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        prevtime=0
        maxdiff=float('-inf')
        minindex=0
        for i,t in events:
            diff=t-prevtime
            if diff==maxdiff:
                minindex=min(minindex,i)
            if diff>maxdiff:
                maxdiff=diff
                minindex=i
            prevtime=t
        return minindex



# Wrong Answer -  206 / 588 testcases passed
# events = [[10,5],[1,7]]
# Output 1
# Expected 10
class Solution2:
    def buttonWithLongestTime(self, events):
        # Initialize max start time and diff as the duration of the first event
        max_time = events[0][0]
        diff = events[0][1] - events[0][0]

        # Loop through the events starting from the second one
        for i in range(1, len(events)):
            current_diff = events[i][1] - events[i][0]

            # If the current difference is greater than the previous diff, update max
            if current_diff > diff:
                max_time = events[i][0]
                diff = current_diff
            # If the current difference is equal to the previous diff, choose the event with the smaller start time
            elif current_diff == diff:
                max_time = min(max_time, events[i][0])

        return max_time  # Return the start time of the event with the longest duration