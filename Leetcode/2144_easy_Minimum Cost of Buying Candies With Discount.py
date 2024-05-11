"""
Done 11.05.2024. Topics: Array, Greedy, Sorting
2144. Minimum Cost of Buying Candies With Discount
https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/description/

A shop is selling candies at a discount.
For every two candies sold, the shop gives a third candy for free.

The customer can choose any candy to take away for free as long as the cost of the chosen candy is less than or
equal to the minimum cost of the two candies bought.

For example, if there are 4 candies with costs 1, 2, 3, and 4, and the customer buys candies with costs 2 and 3,
they can take the candy with cost 1 for free, but not the candy with cost 4.
Given a 0-indexed integer array cost, where cost[i] denotes the cost of the ith candy,
return the minimum cost of buying all the candies.

Example 1:
Input: cost = [1,2,3]
Output: 5
Explanation: We buy the candies with costs 2 and 3, and take the candy with cost 1 for free.
The total cost of buying all candies is 2 + 3 = 5. This is the only way we can buy the candies.
Note that we cannot buy candies with costs 1 and 3, and then take the candy with cost 2 for free.
The cost of the free candy has to be less than or equal to the minimum cost of the purchased candies.

Example 2:
Input: cost = [6,5,7,9,2,2]
Output: 23
Explanation: The way in which we can get the minimum cost is described below:
- Buy candies with costs 9 and 7
- Take the candy with cost 6 for free
- We buy candies with costs 5 and 2
- Take the last remaining candy with cost 2 for free
Hence, the minimum cost to buy all candies is 9 + 7 + 5 + 2 = 23.

Example 3:
Input: cost = [5,5]
Output: 10
Explanation: Since there are only 2 candies, we buy both of them. There is not a third candy we can take for free.
Hence, the minimum cost to buy all candies is 5 + 5 = 10.

Hint 1
If we consider costs from high to low, what is the maximum cost of a single candy that we can get for free?
Hint 2
How can we generalize this approach to maximize the costs of the candies we get for free?
Hint 3
Can “sorting” the array help us find the minimum cost?
"""

# Runtime 23 ms Beats 80.00% of users with Python
# Memory 11.61 MB Beats 37.50% of users with Python

# Sorting from larger to smaller and summing the first two elements in each triple.
# For the last three, we check the existence of these elements

def minimumCost(cost):
    """
    :type cost: List[int]
    :rtype: int
    """
    cost = sorted(cost, reverse=True)
    ll = len(cost)
    if ll<=2: return sum(cost)
    elif ll==3: return cost[0]+cost[1]
    ssum = 0; rr=list(range(0, ll, 3))
    # print(cost, ll, rr,rr[-1])
    for i in rr:
        if i !=rr[-1]:
            ssum = ssum + cost[i]+cost[i+1]
        else:
            if i<ll: ssum=ssum+cost[i]
            if i+1<ll: ssum=ssum+cost[i + 1]
    return ssum



# from https://leetcode.com/u/yw1033/
# https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/solutions/3701723/4-lines-beats-99-runtime/
def minimumCost2(cost):
    cost.sort()
    ll=len(cost); l3=ll % 3
    # print(cost,ll)
    # for i in range(ll):
    #     if i % 3 != l3:
    #         print(i,cost[i])
    #     else:
    #         print('free =',i, cost[i])
    return sum([cost[i] for i in range(ll) if i % 3 != l3])




# print(minimumCost([1,2,3]))
# print(minimumCost([6, 5, 7, 9, 2, 2]))
# print(minimumCost([5,5]))
# print(minimumCost([3,3,3,1]))
print(minimumCost2([10,5,9,4,1,9,10,2,10,8]))