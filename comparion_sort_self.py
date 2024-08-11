'''
#time complexity of the below code is O(n^2)
#[0,1,2,5,7,3,3,2,4]

class Solution:
    def countingSort(self, input: list[int]):
        max_num = max(input)
        output = [0]*len(input)
        aux = [0]*(max_num+1)
        
        for i in input:
            aux[i]+=1
        print (aux)
        k=0
        for i, count in enumerate(aux):
            j=0
            while j < count:
                output[k] = i 
                j , k = j+1, k+1

        print(output)
        
solution = Solution()
solution.countingSort([0,1,2,5,7,3,3,2,4])

'''

#[1,1,0,0,2,3,4,7,8] = [0,0,1,1,2,3,4,7,8]
#aux_list = [2,2,1,1,1,0,0,1,1]

#postition = [2, 4, 5, 6, 7, 7, 7, 8, 9]
class Solution:
    def comparisonSort(self, s: list[int]):
        
        aux_list = [0]*(max(s)+1)
        output = [0]*len(s)
        
        #make a frequency list
        for i in s:
            aux_list[i] +=1
        #print(aux_list)
        
        #position of the element
        temp = 0 
        for i in range(1,len(aux_list)):
            aux_list[i] +=aux_list[i-1]
        print(aux_list)
        
        for i in out          
            
            
        
solution = Solution()
solution.comparisonSort([1,1,0,0,2,3,4,7,8])