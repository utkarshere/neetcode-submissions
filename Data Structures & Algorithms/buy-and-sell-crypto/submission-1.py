class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_prof = 0

        for i in range(len(prices)-1):
            for j in range(i,len(prices)):
                prof = prices[j] - prices[i]
                max_prof = max(max_prof, prof)

        return max_prof

