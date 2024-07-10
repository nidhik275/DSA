class Solution:
    def moveZeroes(self, nums: list) -> None:
        # Initialize the slow pointer to 0
        slow = 0

        # Iterate through the list with the fast pointer
        for fast in range(len(nums)):
            # Check if the current element at fast pointer is non-zero
            # and the current element at slow pointer is zero
            if nums[fast] != 0 and nums[slow] == 0:
                # Swap the elements at slow and fast pointers
                nums[slow], nums[fast] = nums[fast], nums[slow]
                # Increment the slow pointer to the next position
                slow += 1
        return nums
                
solution = Solution()

var_sol = solution.moveZeroes([1,0,1])

print(var_sol)
