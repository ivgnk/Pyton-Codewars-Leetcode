"""
Done 07.07.2024. Topics: Math, Simulation
1518. Water Bottles
https://leetcode.com/problems/water-bottles/description

There are numBottles water bottles that are initially full of water.
You can exchange numExchange empty water bottles from the market with one full water bottle.
The operation of drinking a full water bottle turns it into an empty bottle.
Given the two integers numBottles and numExchange, return the maximum number of water bottles you can drink.

Example 1:
Input: numBottles = 9, numExchange = 3
Output: 13
Explanation: You can exchange 3 empty bottles to get 1 full water bottle.
Number of water bottles you can drink: 9 + 3 + 1 = 13.

Example 2:
Input: numBottles = 15, numExchange = 4
Output: 19
Explanation: You can exchange 4 empty bottles to get 1 full water bottle.
Number of water bottles you can drink: 15 + 3 + 1 = 19.

Constraints:
1 <= numBottles <= 100
2 <= numExchange <= 100
"""


# https://leetcode.com/problems/water-bottles/description/comments/2498131
# Runtime 7 ms Beats 95.45% Analyze Complexity
# Memory 11.48 MB Beats 84.09%

def numWaterBottles1(numBottles, numExchange):
    """
    :type numBottles: int
    :type numExchange: int
    :rtype: int
    """
    return (numBottles * numExchange - 1) / (numExchange - 1)

# Runtime 7 ms Beats 95.45%
# Memory 11.43 MB Beats 84.09%
def numWaterBottles(numBottles, numExchange):
    """
    :type numBottles: int
    :type numExchange: int
    :rtype: int
    """
    ssum = 0
    empty=10000
    ost=0
    while empty >= numExchange:
        ssum += numBottles - ost
        ost = numBottles - (numBottles // numExchange * numExchange)
        empty = numBottles
        numBottles = empty / numExchange + ost
    return ssum

# print(numWaterBottles(numBottles = 9, numExchange = 3))
print(numWaterBottles(numBottles = 15, numExchange = 4))
