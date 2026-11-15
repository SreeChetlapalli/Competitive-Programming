class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            x = target - nums[i]
            if x in nums[0:i] + nums[i+1:]:
                y = nums.index(x)

                if y > i:
                    return [i,y]
                else:
                    return [y,i]
            x = target
        return []
        