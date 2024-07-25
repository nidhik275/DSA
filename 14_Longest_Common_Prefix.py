'''
Input: strs = ["flower","flow","flight"]
Output: "fl"
'''

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        longest = ""

        min_string = min(len(s) for s in strs)
        
        for i in range(min_string):
            for j in strs:
                if j[i]!= strs[0][i]:
                    return longest
                
            longest += strs[0][i]
        return longest
            
            
                      
solution = Solution()
longest_prefix = solution.longestCommonPrefix(["flower","flow","flight"])

print(longest_prefix)
