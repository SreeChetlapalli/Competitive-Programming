class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        x = 0
        y = 1
        z = len(nums)-1
        nums.sort()
        lists = []
        sets=()
        while x < 0:
            if nums[x]+nums[y]+nums[z]>0:
                z-=1
            if nums[x]+nums[y]+nums[z]<0:
                y+=1
            if y == z:
                while nums[x+1] == nums[x]:
                    x+=1
                
                y = x+1
                z = len(nums)-1
            if nums[x]+nums[y]+nums[z]==0:
                lists.append([nums[x],nums[y],nums[z]])
        return lists


                