''''
Example 1:

Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
Output: [4,0,3]
Explanation:
- 0th spell: 5 * [1,2,3,4,5] = [5,10,15,20,25]. 4 pairs are successful.
- 1st spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
- 2nd spell: 3 * [1,2,3,4,5] = [3,6,9,12,15]. 3 pairs are successful.
Thus, [4,0,3] is returned.
Example 2:

Input: spells = [3,1,2], potions = [8,5,8], success = 16
Output: [2,0,2]
Explanation:
- 0th spell: 3 * [8,5,8] = [24,15,24]. 2 pairs are successful.
- 1st spell: 1 * [8,5,8] = [8,5,8]. 0 pairs are successful. 
- 2nd spell: 2 * [8,5,8] = [16,10,16]. 2 pairs are successful. 
Thus, [2,0,2] is returned.

'''

# generalised code
class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        output = [0]*len(spells)
        temp=[0]*len(potions)
        for i in range(len(spells)):
            res = 0
            for j in range(len(potions)):
                res = spells[i]*potions[j]
                temp[j] = res
            #check how many elements are bigger than success
            res = 0 
            for j in temp:
                if j>=success:
                    res+=1
            output[i] = res
            
            #print(temp)
        return output
            
solution  = Solution()
output = solution.successfulPairs([3,1,2],[8,5,8],16)

print(output)