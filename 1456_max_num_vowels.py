#sliding window protocol 

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        #vowels = ['a','e','i','o','u']
        vowels = {'a','e','i','o','u'}
        count = 0
        
        for i in range(k):
            if s[i] in vowels:
                count +=1

        max_vowel = count 
        for i in range(len (s) - k):
            if s[i] in vowels:
                count -=1
            if s[i+k] in vowels:
                count +=1
            max_vowel = max(max_vowel, count)
        return max_vowel

solution = Solution()

max_vowel = solution.maxVowels('leetcode', 3)
print (max_vowel)