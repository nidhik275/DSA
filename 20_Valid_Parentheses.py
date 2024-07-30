'''
Input: s = "()"
Output: true


'(', ')', '{', '}', '[' and ']'

'''

class Solution:
    def isValid(self, s: str) -> bool:
        set = {
            ')':'(',
            '}':'{',
            ']':'['
               }
        temp = []
        
        for i in s:
            if i in '{([':
                temp.append(i)
            else:
                open_bracket = temp.pop()
                if open_bracket != set[i]:
                    #print(set[])
                #print(set[i])    
                    return False
        return True
    
soltuion = Solution()

output = soltuion.isValid('()')
print(output)
                    
        
        
        