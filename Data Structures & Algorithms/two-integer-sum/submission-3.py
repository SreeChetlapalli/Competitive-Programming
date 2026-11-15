class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        x = {}
        for i in range(len(nums)):
            
            y = target - nums[i]
            if y in x:
                return [x[y], i]
            x[nums[i]] = i

        return []       

