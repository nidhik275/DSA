class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        new_flower = 0 
        curr_pointer = 0 
        length = len(flowerbed)#7
        for curr_pointer in range(length):
            if length == 1:
                if flowerbed[0] == 0:
                    new_flower +=1
                    break
                else:
                    return False
            if (curr_pointer == length -1 and flowerbed[curr_pointer -1]==0 and flowerbed[curr_pointer]==0) or (curr_pointer == 0 and flowerbed[curr_pointer +1]==0 and flowerbed[curr_pointer]==0) or (flowerbed[curr_pointer] == 0 and flowerbed[curr_pointer +1]==0 and flowerbed[curr_pointer -1] ==0):
                flowerbed[curr_pointer] =1
                new_flower +=1
        if n<=new_flower:
            return True
        else:
            return False

solution = Solution()
ans = solution.canPlaceFlowers([1,0,0,0,1,0,0],1)
print(ans)   