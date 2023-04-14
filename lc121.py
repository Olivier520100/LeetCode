class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        currentmax = 0
        minpointer = 0
        currentpointer = 1
        while (currentpointer < len(prices)):
            if (prices[minpointer] > prices[currentpointer]):
                minpointer = currentpointer
            
            currentmax = max(currentmax, prices[currentpointer] - prices[minpointer])

            
            currentpointer +=1

        return currentmax
