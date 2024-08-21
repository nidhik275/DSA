class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        potions = sorted(potions)
        start = 0 
        temp = len(potions)
        result = []
        end = len(potions) - 1
        for i in spells:
            while start<=end: 
                mid = (start+ end)//2
                if i * potions[mid]>=success: 
                    temp = mid 
                    end = mid -1
                else: 
                    start = mid + 1
            result.append(len(potions)-temp)
        return result
    
solution = Solution() 
output = solution.successfulPairs([5,1,3],[1,2,3,4,5],7)
print(output)
                
            
