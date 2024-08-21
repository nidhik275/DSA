'''
Author: Nidhi Kumari
Problem: Bubble sort 

Attempt 1

'''

class Solution: 
    def bubbleSort(self, input: list[int]):
        length = len(input)
        for i in range(length):
            i = 0
            while i < (length-1):
            
                if input[i]>input[i+1]:
                    input[i], input[i+1] = input[i+1], input[i]
                i+=1
            length-=1
        return input
solution = Solution()
output = solution.bubbleSort([2,3,5,1,11,6,4])
print (output)



'''
#Optimised code by chatgpt

class Solution: 
    def bubbleSort(self, input: list[int]):
        length = len(input)
        for i in range(length):
            swapped = False
            for j in range(0, length - i - 1):  # Reduce the range with each pass
                if input[j] > input[j + 1]:
                    input[j], input[j + 1] = input[j + 1], input[j]
                    swapped = True
            if not swapped:  # If no two elements were swapped, break the loop
                break
        return input

solution = Solution()
output = solution.bubbleSort([2, 3, 5, 1, 11, 6, 4])
print(output)

'''