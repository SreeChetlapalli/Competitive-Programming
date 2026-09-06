class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left = 0
        right = len(prices)-1

        while right > left:
            if prices[left+1] < prices[left]:
                left +=1  
            if prices[right-1] > prices[right]:
                right -=1
            if prices[left+1] >= prices[left] and prices[right-1] <= prices[right]:
                break

        if prices[left]-prices[right] > prices[right]:
            return 0 
        return abs(prices[left]-prices[right]        )       