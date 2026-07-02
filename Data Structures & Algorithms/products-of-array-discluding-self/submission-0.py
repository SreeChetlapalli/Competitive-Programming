class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 2:
            return [nums[1], nums[0]]
        
        count = 0
        x=[1] * (len(nums))
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j == i and count != 1:
                    count +=1
                    continue
                else:
                    x[i] *= nums[j]
            count = 0
        
        return x


        