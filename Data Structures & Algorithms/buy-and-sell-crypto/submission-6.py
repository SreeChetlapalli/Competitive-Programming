class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mins = float('inf')
        p = 0
        for i in prices:
            if i < mins:
                mins = i 
            if i-mins > p:
                p = i-mins

        return p
            