class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        x = 0
        y = {}
        f = []
        for i in nums:
            x = i
            num1 = nums[:i]+nums[i+1:]
            for j in num1:
                complement = x - j
                if complement in y:
                    f.append[i, j, y[complement]]
        return f






        