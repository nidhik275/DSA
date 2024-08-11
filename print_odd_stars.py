'''
Option one
class Solution:
    def printStar(self, n: int):
        space = n -1
        for i in range(n):
            #for j in range(n-1, 1)
            j = 0 
            while j < space:
                print(" ", end="")
                j+=1
            space -=1
            stars = 2*i +1
            m = 0
            while m < stars:
                print("*", end="")
                m+=1
            print('\n')
            
solution = Solution()
solution.printStar(5)
'''

#option 2 - optimised
class Solution:
    def printStar(self, n: int):
        
        for i in range(n):
            print(" " * (n - i - 1), end="")
            print("*"* (2*i + 1))

solution = Solution()
solution.printStar(5)
