"""
Done 22.06.2024. Topics: Array, Sorting
1833. Maximum Ice Cream Bars
https://leetcode.com/problems/maximum-ice-cream-bars/description/

It is a sweltering summer day, and a boy wants to buy some ice cream bars.
At the store, there are n ice cream bars. You are given an array costs of length n,
where costs[i] is the price of the ith ice cream bar in coins.
The boy initially has coins coins to spend, and he wants to buy as many ice cream bars as possible.

Note: The boy can buy the ice cream bars in any order.
Return the maximum number of ice cream bars the boy can buy with coins coins.
You must solve the problem by counting sort.

Example 1:
Input: costs = [1,3,2,4,1], coins = 7
Output: 4
Explanation: The boy can buy ice cream bars at indices 0,1,2,4 for a total price of 1 + 3 + 2 + 1 = 7.

Example 2:
Input: costs = [10,6,8,7,7,8], coins = 5
Output: 0
Explanation: The boy cannot afford any of the ice cream bars.

Example 3:
Input: costs = [1,6,3,1,2,5], coins = 20
Output: 6
Explanation: The boy can buy all the ice cream bars for a total price of 1 + 6 + 3 + 1 + 2 + 5 = 18.

Hint 1
It is always optimal to buy the least expensive ice cream bar first.
Hint 2
Sort the prices so that the cheapest ice cream bar comes first.
"""

# Runtime 610 ms Beats 90.07%
# Memory 30.35 MB Beats 69.87%

def maxIceCream(costs, coins):
    """
    :type costs: List[int]
    :type coins: int
    :rtype: int
    """
    ll=len(costs)
    costs.sort()
    n=0; i=0
    while i<ll and costs[i]<=coins:
        coins=coins-costs[i]
        n=n+1
        i=i+1
    return  n

# print(maxIceCream(costs = [1,3,2,4,1], coins = 7)) # 4
print(maxIceCream(costs = [10,6,8,7,7,8], coins = 5)) # 0
print(maxIceCream(costs = [1,6,3,1,2,5], coins = 20))
