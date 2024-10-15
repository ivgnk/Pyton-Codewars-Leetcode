"""
Done 15.10.2024. Topics: Array
57. Insert Interval
https://leetcode.com/problems/insert-interval/description/
You are given an array of non-overlapping intervals intervals
where intervals[i] = [starti, endi] represent the start and the end of the ith interval and
intervals is sorted in ascending order by starti.
You are also given an interval newInterval = [start, end]
that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is
still sorted in ascending order by starti and intervals still does not have any
overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Constraints:
0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 105

Hint 1
Intervals Array is sorted. Can you use Binary Search to find the correct
position to insert the new Interval.?
Hint 2
Can you try merging the overlapping intervals while inserting the new interval?
Hint 3
This can be done by comparing the end of the last interval with the start of
the new interval and vice versa.

My solution
https://leetcode.com/problems/insert-interval/solutions/5915077/python-solution-problem-0057-without-binary-search/

✏️ Python solution Problem 0057 without binary search
Intuition
The main thing is that there is no TLE & MLE
The limitations of the task make it possible not to use binary search

Approach
- append newInterval
- sort intervals
- find ovelapping intervals and merge it
N.B.: binary search is not on topics
"""

# Runtime 69 ms Beats 28.84%
# Memory 15.20 MB Beats 22.36%
def insert(intervals, newInterval):
    """
    :type intervals: List[List[int]]
    :type newInterval: List[int]
    :rtype: List[List[int]]
    """
    intervals.append(newInterval)
    intervals.sort()
    i=1
    while i<len(intervals):
        # print(i,intervals)
        if not intervals[i-1][1]<intervals[i][0]:
            nint=[min(intervals[i-1][0],intervals[i][0]),max(intervals[i-1][1],intervals[i][1])]
            del intervals[i]
            del intervals[i-1]
            intervals.insert(i-1,nint)
        else:
            i+=1
    return intervals

# print(insert(intervals = [[1,3],[6,9]], newInterval = [2,5]))
print(insert(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]))



