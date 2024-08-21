class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        potions.sort()
        
        result = []
        
        for i in spells:
            start = 0 
            end = len(potions) - 1
            temp = len(potions)
            while start<=end: 
                mid = (start+ end)//2
                if i * potions[mid]>=success: 
                    temp = mid 
                    end = mid -1
                else: 
                    start = mid + 1
            result.append(len(potions)-temp) #once you have the index of mid, then subtracting mid from lenghth will give you the numbers which will give greated product than success
            #eg: [1,1,2,2,2,3,4,5]
            #         |
            #        mid
            #len(potion) = 8 - 2 = 6, numbers when multiplied with spells which give >=7
        return result
    
solution = Solution() 
output = solution.successfulPairs([5,1,3],[1,2,3,4,5],7)
print(output)
                
            
