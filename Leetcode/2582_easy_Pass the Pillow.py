"""
Done 06.07.2024. Topics: Math, Simulation
There are n people standing in a line labeled from 1 to n.
The first person in the line is holding a pillow initially.
Every second, the person holding the pillow passes it to the next person standing in the line.
Once the pillow reaches the end of the line, the direction changes, and people continue
passing the pillow in the opposite direction.
For example, once the pillow reaches the nth person they pass it to the n - 1th person,
then to the n - 2th person and so on.
Given the two positive integers n and time, return the index of the person holding the pillow after time seconds.

Example 1:
Input: n = 4, time = 5
Output: 2
Explanation: People pass the pillow in the following way: 1 -> 2 -> 3 -> 4 -> 3 -> 2.
After five seconds, the 2nd person is holding the pillow.

Example 2:
Input: n = 3, time = 2
Output: 3
Explanation: People pass the pillow in the following way: 1 -> 2 -> 3.
After two seconds, the 3rd person is holding the pillow.

Hint 1
Maintain two integer variables, direction and i, where direction denotes the current direction
in which the pillow should pass, and i denotes an index of the person holding the pillow.
Hint 2
While time is positive, update the current index with the current direction.
If the index reaches the end of the line, multiply direction by - 1.
"""

# Runtime 12 ms Beats 71.25%
# Memory 11.60 MB Beats 61.25%
# Runtime 8 ms Beats 91.25%
# Memory 11.61 MB Beats 23.75%

def passThePillow(n, time):
    """
    :type n: int
    :type time: int
    :rtype: int
    """
    i = 1; t=1; direction = -1
    while t <=time:
        if i == n or i == 1:
            direction = -direction
        i = i + direction
        t = t + 1
    return i

print(passThePillow(4,5))
print(passThePillow(3,2))