class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxprrfit = 0
        for i in range(1,len(prices)):
            profit = prices[i] - prices[i-1]
            if profit > 0:
                maxprrfit += profit
        return maxprrfit