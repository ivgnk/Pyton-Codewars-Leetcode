"""
29.08.2024. Topics: Queue

933. Number of Recent Calls
https://leetcode.com/problems/number-of-recent-calls/description/

You have a RecentCounter class which counts the number of recent
requests within a certain time frame.
Implement the RecentCounter class:

RecentCounter() Initializes the counter with zero recent requests.
int ping(int t) Adds a new request at time t, where t represents some time in milliseconds,
and returns the number of requests that has happened in the past 3000 milliseconds (including the new request).
Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.

Example 1:
Input
["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]
Output
[null, 1, 2, 3, 3]

Explanation
RecentCounter recentCounter = new RecentCounter();
recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2
recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3
recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is [2,3002], return 3

Constraints:
1 <= t <= 109
Each test case will call ping with strictly increasing values of t.
At most 104 calls will be made to ping.
"""

from collections import deque

# Runtime 219 ms Beats 51.05%
# Memory 16.44 MB Beats 93.36%
# https://leetcode.com/problems/number-of-recent-calls/solutions/5686896/python/
class RecentCounter(object):
    def __init__(self):
        self.request = []

    def ping(self, t):
        self.request.append(t)
        while self.request[0] < t - 3000:
            self.request.pop(0)
        return len(self.request)

# https://leetcode.com/problems/number-of-recent-calls/description/comments/2033605

# Runtime 2054 ms Beats 13.88%
# Memory 16.95 MB Beats 12.19%
class RecentCounter4(object):
    def __init__(self):
        self.time=deque()

    def ping(self, t):
        self.time.appendleft(t)
        n=0
        for i in self.time:
            if i >=t-3000: n=n+1
            else: break
        return n



# Runtime 3704 ms Beats 9.07%
# Memory 17.06 MB Beats 5.55%
class RecentCounter2(object):
    def __init__(self):
        self.time=[]

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.time.append(t); n=0
        for i in list(reversed(self.time)):
            if i >=t-3000: n=n+1
            else: break
        return n

# Runtime 2095 ms Beats 13.81%
# Memory 17.04 MB Beats 5.55%
class RecentCounter3(object):
    def __init__(self):
        self.time=[]

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.time.insert(0,t); n=0
        for i in self.time:
            if i >=t-3000: n=n+1
            else: break
        return n

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)