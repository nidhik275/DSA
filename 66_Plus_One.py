'''
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        length = len(digits)
        temp = [1]
        if digits[length -1] == 9:
            for i in reversed(range(length)): 
                if digits[i] == 9:
                    digits[i] = 0
                    if i == 0:
                        digits = temp+digits    
                else:
                    digits[i] +=1
        else:
            digits[i] +=1
            
        return digits
'''

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        length = len(digits)

        for i in reversed(range(length)): 
            if digits[i] == 9:
                digits[i] = 0  
            else:
                digits[i] +=1
                return digits
            
        return [1] + digits