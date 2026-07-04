class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = set(nums)
        count = 0
        d = defaultdict(list)
        
        for i in num:
            if i-1 not in num:
                length = 0 
                while (i+length) in num:
                    length+=1
                count = max(count, length)

        return count