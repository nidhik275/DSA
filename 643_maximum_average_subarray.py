'''
Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:

Input: nums = [5], k = 1
Output: 5.00000

'''

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        max_sum = 0 
        initial_sum = sum(nums[:k])
        max_sum = initial_sum
        window_sum = 0
        for j in range(len(nums)-k):
            window_sum = window_sum + nums[j + k] - nums[j]
            max_sum = max(window_sum, max_sum)
        
        return max_sum/k     