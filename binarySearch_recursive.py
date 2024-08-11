'''

sorted array = [-20,1,3,5,7,11,14,18,110]
x = 1
start = 0 
end = 9-1 = 8 
mid = (0+8)/2 = 4 

'''

class Solution:
    def binarySearch(self, arr: list[int],x, start, end):
        mid = start + (end - start)//2 # (2start + end - start)/2 = (start + end)/2
        if arr[mid] == x: #found the element
           return mid
        elif arr[mid]> x: 
           return self.binarySearch (arr,x,start,mid-1)
        else:
            return self.binarySearch(arr, x, mid+1, end)
        
arr = [-20,1,3,5,7,11,14,18,110]
find = 3

solution = Solution()

index = solution.binarySearch(arr,find,0, len(arr)-1)
print("found element "+str(find)+ " at index "+ str(index))     
