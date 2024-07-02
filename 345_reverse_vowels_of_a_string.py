class Solution:
    def reverseVowels(self, s: str) -> str:  # Define a method to reverse vowels in a string
        s = list(s)  # Convert the string to a list to allow in-place modification
        left = 0  # Initialize the left pointer at the beginning of the list
        right = len(s) - 1  # Initialize the right pointer at the end of the list
        m = 'aeiouAEIOU'  # A string containing all the vowels (both lowercase and uppercase)
        
        while left < right:  # Continue until the two pointers meet
            if s[left] in m and s[right] in m:  # If both characters at the left and right pointers are vowels
                s[left], s[right] = s[right], s[left]  # Swap the vowels
                left = left + 1  # Move the left pointer to the right
                right = right - 1  # Move the right pointer to the left
                
            elif s[left] not in m:  # If the character at the left pointer is not a vowel
                left = left + 1  # Move the left pointer to the right
                
            elif s[right] not in m:  # If the character at the right pointer is not a vowel
                right = right - 1  # Move the right pointer to the left
        
        return ''.join(s)  # Convert the list back to a string and return it
     
# Create an instance of the Solution class
solution = Solution()

# Call the reverseVowels method with a test string
rev_str = solution.reverseVowels("Leetcode")

print(rev_str)  # Expected output: "Leotcede"