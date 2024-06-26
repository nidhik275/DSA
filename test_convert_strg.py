class Solution:
    def convert(self, s: str, numRows: int)-> str:
        step = 0
        index = 0 
        
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