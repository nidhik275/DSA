class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        i =0 
        while i in range(len(flowerbed)):
            if flowerbed[i] ==0:
                prev = flowerbed[i-1] if i>0 else 0
                next = flowerbed[i+1] if i< len(flowerbed) -1 else 0 
                
                if next ==0 and prev ==0:
                    flowerbed[i] = 1
                    count +=1
                    if count >=n:
                        return True
        
        return False
    
'''
Approach 2 

class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        f = [0] + flowerbed + [0]
        
        for i in range(1,len(f)-1):
            if f[i-1]==0 and f[i] == 0 and f[i+1] ==0:
                f[i] =1
                n -=1
        return n<=0

'''
                    