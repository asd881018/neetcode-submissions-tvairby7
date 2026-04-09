class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # find the cheaper starting price
        # then find the highest profit after that cheap buying price

        if (len(prices) < 2):
            return 0

        l, r = 0, 1
        maxProfit = 0
        
        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            else:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            r += 1

        return maxProfit
