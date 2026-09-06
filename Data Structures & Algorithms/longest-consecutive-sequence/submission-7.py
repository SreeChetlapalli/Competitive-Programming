class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
            
        x = (nums)
        
        
        x.sort()

        d = defaultdict(set)
        count = 0

        for i in range(len(x)-1):
            if x[i+1] -x[i] == 1:
                d[count].add(x[i],x[i+1])
            else:
                count += 1
        
        z = max(len(v) for v in d.values())

        return z

