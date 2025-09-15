from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        so = ''
        pre = {}

        for word in strs:
            i = 0
            while i < len(word):
                if word[i] in pre and pre[word[i]] == i:
                    so = so + word[i]
                    print(so)
                else:
                    pre[word[i]] = i
                i += 1
                
        print(pre)
        
        return so
    
strs = ["flower","flow","flight"]

sol = Solution()
s = sol.longestCommonPrefix(strs)

print(s)