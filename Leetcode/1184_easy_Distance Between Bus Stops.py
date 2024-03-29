'''
1184. Distance Between Bus Stops
https://leetcode.com/problems/distance-between-bus-stops/description/

A bus has n stops numbered from 0 to n - 1 that form a circle.
We know the distance between all pairs of neighboring stops where distance[i]
is the distance between the stops number i and (i + 1) % n.
The bus goes along both directions i.e. clockwise and counterclockwise.

Return the shortest distance between the given start and destination stops.

Example 1:
Input: distance = [1,2,3,4], start = 0, destination = 1
Output: 1
Explanation: Distance between 0 and 1 is 1 or 9, minimum is 1.

Example 2:
Input: distance = [1,2,3,4], start = 0, destination = 2
Output: 3
Explanation: Distance between 0 and 2 is 3 or 7, minimum is 3.

Example 3:
Input: distance = [1,2,3,4], start = 0, destination = 3
Output: 4
Explanation: Distance between 0 and 3 is 6 or 4, minimum is 4.
'''

# Runtime 22 ms Beats 85.96% of users with Python
# Memory 12.43 MB Beats 85.96% of users with Python

def distanceBetweenBusStops(dis, st, dt):
    """
    :type distance: List[int]
    :type start: int
    :type destination: int
    :rtype: int
    """
    llen=len(dis)
    if st>dt: st,dt = dt, st
    s1 = sum([dis[i] for i in range(st, dt)])
    s2 = sum([dis[i] for i in range(dt, llen)])+sum([dis[i] for i in range(0, st)])
    return min(s1, s2)

#   0  1 2  3  4  5 6 7
#  [7,10,1,12,11,14,5,0]
print(distanceBetweenBusStops(dis =[7,10,1,12,11,14,5,0], st = 7, dt = 2))