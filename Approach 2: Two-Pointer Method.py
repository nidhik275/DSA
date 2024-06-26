'''Approach 2: Two-Pointer Method
Initialize two pointers, i and j, both initially set to 0.
Move the pointer that corresponds to the smaller value forward at each step.
Continue moving the pointers until you have processed half of the total number of elements.
Calculate and return the median based on the values pointed to by i and j.
Time Complexity

O(n + m), where ‘n’ & ‘m’ are the sizes of the two arrays.
Space Complexity

O(1).'''
'''
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        n = len(nums1)
        m = len(nums2)
        i = 0
        j = 0
        m1 = 0
        m2 = 0

        # Find median.
        for count in range(0, (n + m) // 2 + 1):
            m2 = m1
            if i < n and j < m:
                if nums1[i] > nums2[j]:
                    m1 = nums2[j]
                    j += 1
                else:
                    m1 = nums1[i]
                    i += 1
            elif i < n:
                m1 = nums1[i]
                i += 1
            else:
                m1 = nums2[j]
                j += 1

        # Check if the sum of n and m is odd.
        if (n + m) % 2 == 1:
            return float(m1)
        else:
            ans = float(m1) + float(m2)
            return ans / 2.0
            
'''

#nums1 = [1,3,5]
#nums2 = [2,3,4,6,7]
#result = [1,2,3,3,4,5,6,7] => median =[3,4] = 8/2 = 4
 
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        index =0
        i = j = 0
        m = len(nums1)
        n = len(nums2)
        curr = prev =0 
        while index in range((m+n)//2+ 1):
            prev = curr
            if i<m and i<n: 
                if nums1[i] < nums2[j]: 
                    curr = nums1[i]
                    i +=1
                else:
                    curr = nums2[j]
                    j+=1
            elif i<m: #num2 is exhausted
                curr = nums1[i]
                i+=1
            else: #num1 is exhausted 
                curr = nums2[j]
                j+=1      
                            
            #index to run while loop which is median of the both the array combined    
            index +=1
        
        if (m+n)%2 == 0: #length of the final array is even hence two elements sum will be the median 
            return (float(curr) + float(prev))/2.0
        else: #odd
            return float(curr)

solution = Solution()

print(solution.findMedianSortedArrays([1,2],[3,4]))
        
    










































