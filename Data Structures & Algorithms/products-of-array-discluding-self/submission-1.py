class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        first = [1]*len(nums)
        x = 1
        y=1
        last = [1]*len(nums)

        for i in range(len(nums)): 
            y *= nums[i]
            first[i] = y

        for i in range(len(nums)-1,-1, -1): 
            x *= nums[i]
            last[i] = x
        
        z = [1]*len(nums)
        j = len(last)
        for i in range(len(nums)):
            left  = first[i-1] if i > 0 else 1
            right = last[i+1]  if i < len(nums)-1 else 1
            z[i]  = left * right
        return z
        
        