class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        L = 0

        for R in range(1,len(prices)):
            p = prices[R] - prices[L]
            if p < 0:
                L = R
            else:
                res = max(res, p)
        return res

        