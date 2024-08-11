#1207. Unique Number of Occurrences

class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        #arr1 = set(arr)
        occurance = {}
        '''
        for i in arr1:
            occurance[i] = 0 
        print(occurance)
        
        for i in arr:
            occurance[i]+=1
        print(occurance)
        print(arr1)
        '''
        for i in arr:
            if i == occurance:
                occurance[i]+=1
            else:
                occurance[i] = 1
                
        #print(occurance)
        
        if len(occurance) == len(set(occurance.values())):
            return True
        else:
            return False


        
solution = Solution()
output = solution.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0])
print(output)
        