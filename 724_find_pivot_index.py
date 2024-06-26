
class Solution:
    def pivotIndex(self, nums):
        right_sum = left_sum = pivot=0
        left_sum = sum(nums)
        print(left_sum)
        
        while pivot<len(nums):
            if pivot != 0: 
                #left_sum = left_sum - nums[pivot]
                right_sum = right_sum + nums[pivot - 1]
            '''else:
                right_sum = right_sum + nums[pivot - 1]
                left_sum = left_sum - nums[pivot]
            '''
            left_sum = left_sum - nums[pivot]
            
            if right_sum == left_sum:
                return pivot
            pivot = pivot + 1
    
        return -1
     
solution = Solution()  
result = solution.pivotIndex([1,7,3,6,5,6]) 

print(result)