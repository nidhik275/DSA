class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0 
        #second = 0 
        counter = len(nums)-1
        #handle the edge case where the only element of the array is zero
        if len(nums) != 1:
            while index<counter:
                if nums[index] == 0:
                    first = index
                    second = index+1
                    while second <=counter:
                        nums[first], nums[second]= nums[second], nums[first] #swap
                        first +=1
                        second+=1
                    counter -=1 #reduce the counter as now the last number is zero
                else:
                    index +=1
                    
        return nums
    
solution = Solution()
val = solution.moveZeroes([0,1,0,3,12])
print(val)
        
                
                