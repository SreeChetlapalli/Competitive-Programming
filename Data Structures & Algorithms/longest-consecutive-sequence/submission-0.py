class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        x = (nums)
        
        
        x.sort()

        d = defaultdict(list)
        count = 0

        for i in range(len(x)-1):
            if x[i+1] -x[i] == 1:
                d[count].append(x[i])
            else:
                count += 1
        
        z = max(len(v) for v in d.values())

        return z+2

