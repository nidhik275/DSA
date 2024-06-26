class Solution: 
    def findMed(self, nums1, nums2):
        i =j = 0 
        index =0 
        final_array = []
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                final_array.append(nums1[i])
                i+=1
            else:
                final_array.append(nums2[j])
                j+=1
            
        print(final_array)
        final_array.extend(nums1[i:])
        final_array.extend(nums2[j:])
        
        print(final_array)
        #find the median 
        final_array_len = len(final_array)
        if final_array_len %2 == 0:
            return (float(final_array[(final_array_len//2)-1]) + float(final_array[final_array_len//2]))/ 2.0
        else:
            return float(final_array[final_array_len//2])

solution = Solution()

print(solution.findMed([1,3],[2,4]))

