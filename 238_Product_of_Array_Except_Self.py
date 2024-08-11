'''
Author: Nidhi
level: medium 

Problem:
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

'''
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # Get the length of the input list
        n = len(nums)
        
        # Initialize the prefix and postfix products to 1
        prefix_product = 1
        postfix_product = 1
        
        # Initialize the result list with zeros, of the same length as nums
        result = [0] * n
        
        # First pass: Calculate the prefix products
        for i in range(n):
            # Store the current prefix product in result[i]
            result[i] = prefix_product
            # Update the prefix product by multiplying with the current element
            prefix_product *= nums[i]
        
        # Second pass: Calculate the postfix products
        for i in range(n - 1, -1, -1):
            # Multiply the current postfix product with the corresponding value in result
            result[i] *= postfix_product
            # Update the postfix product by multiplying with the current element
            postfix_product *= nums[i]
        
        # Return the final result list
        return result
    
    
    
solution = Solution()
output = []
output = solution.productExceptSelf([-1,1,0,-3,3])
print(output)

'''
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        total = 1
        for i in nums:
            total *= i
        
        answer = []
        for i in range(len(nums)):
            answer.append(total//nums[i])
            
        return answer

solution = Solution()
output = []
output = solution.productExceptSelf([-1,1,0,-3,3])
print(output)
'''