#P A Y P A L I S H I R I N G
#1 2 3 4 3 2 1 2 3 4 3 2 1 2

#list comprehension https://www.freecodecamp.org/news/list-comprehension-in-python-with-code-examples/
# youtube https://www.youtube.com/watch?v=ytSl-K4xo3w 

class Solution:
    def convert(self, s: str, numRows: int)-> str:
        step = 0
        index = 0 
        
        #if numRows is 1 or there is only one charachter in 's'
        if numRows == 1 or numRows >= len(s) or len(s) == 1:
            return s
        
        result = [[] for j in range(numRows)]
        print(result)
        
        for i in s:
            
            result[index].append(i) 
            #when index is 0 then incerament it 
            if index == 0: 
                step = 1
            elif index == numRows -1:
                step = -1
            index = index + step
            
        #concatinate the string
        for k in range(numRows): 
            result[k] = ''.join(result[k])
        return ''.join(result)
                                                          
solution = Solution()

print(solution.convert('PAYPALISHIRING',3))
            