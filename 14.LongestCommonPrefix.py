from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        so = ''

        for i in range(len(strs)):
            for j in strs[i]:
                print(j)

        
        return so
    
strs = ["flower","flow","flight"]

sol = Solution()
s = sol.longestCommonPrefix(strs)

print(s)