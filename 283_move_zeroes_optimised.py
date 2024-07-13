'''
[0,1,0,3,12]
[1,0,1]
'''

class Solution: 
    def moveZeroes(self, nums: list):
        slow =0
        fast = 0 
        for fast in range(len(nums)):
            if nums[fast]!=0 and nums[slow] == 0:
                #swap
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow +=1
            if nums[slow]!=0 and nums[fast]!=0:
                slow +=1
                
solution = Solution()
nums = [0,1,0,3,12]
solution.moveZeroes(nums)
print(nums)