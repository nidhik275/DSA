'''
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

'''


class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        count = 0  

        for i in range(len(s)):
            if i < (len(s)-1) and roman[s[i]]<roman[s[i+1]]:
                count -=roman[s[i]]
            else:
                count += roman[s[i]]
        return count 
                  
solution = Solution()
value = solution.romanToInt('LVIII')
print (value)