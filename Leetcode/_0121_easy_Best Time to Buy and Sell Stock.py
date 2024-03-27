'''
121. Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and
choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
'''

# Time Limit Exceeded,  200 / 212 testcases passed

def maxProfit2(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    dsc = sorted(prices,reverse=True)
    if prices==dsc: return 0
    llen= len(prices); print(llen)
    asc = sorted(prices)
    if prices==asc: return prices[llen-1]-prices[0]
    profit = -100000
    # print('ini=',prices)
    for i in range(llen):
        mmin=prices[i]
        pr = prices[i+1:]
        if pr !=[]:
            mmax=max(pr)
            cpr=mmax-mmin
            if (cpr>profit) and (cpr>=0):
                profit=cpr
                # print(i,profit)
    return profit

def maxProfit3(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    dsc = sorted(prices,reverse=True)
    if prices==dsc: return 0
    llen= len(prices);
    asc = sorted(prices)
    if prices==asc: return prices[llen-1]-prices[0]
    profit = -100000
    # print('ini=',prices)
    while llen>1:
        mmin=prices[0]
        pr = prices[1:]
        if pr !=[]:
            mmax=max(pr)
            cpr=mmax-mmin
            if (cpr>profit) and (cpr>=0):
                profit=cpr
                # print(i,profit)
        prices=pr
        llen=llen-1
    return profit

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    dsc = sorted(prices,reverse=True)
    if prices==dsc: return 0
    llen= len(prices);
    asc = sorted(prices)
    if prices==asc: return prices[llen-1]-prices[0]
    profit = -100000
    # print('ini=',prices)
    i = 0
    while llen>1:
        mmin=min(prices)
        ind= prices.index(mmin)
        pr = prices[ind+1:]
        if pr !=[]:
            mmax=max(pr)
            cpr=mmax-mmin
            if (cpr>profit) and (cpr>=0):
                profit=cpr
                # print(mmin,mmax,profit)
        del prices[ind]
        llen=len(prices)
        print(i,profit)
        i=i+1
    return profit


# print(maxProfit([7,6,4,3,1]))
# print(maxProfit([1,3,4,6,7]))
# prices=[7,1,5,3,6,4]
# mmin=min(prices)
# print(prices.index(mmin))
# print(f'{maxProfit([7,1,5,3,6,4])=}')
print(f'{maxProfit([3,2,6,5,0,3])=}')
