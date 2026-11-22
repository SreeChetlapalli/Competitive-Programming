class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        x ={}

        for i in range(len(nums)):
            if nums[i] in x.keys():
                x[nums[i]] += 1
            else:
                x[nums[i]] = 1
        
        z = sorted(x.keys())

        return z[:-k-1:-1]
        