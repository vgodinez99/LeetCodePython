class Solution:
    def isPalindrome(self, x: int) -> bool:

        self.x = x

        y = str(x)
        z = ''

        for i in reversed(y):
            z = z + i

        if y == z:
            sol = True
        else:
            sol = False
        
        return sol
    
x = 10000001

sol = Solution()
s = sol.isPalindrome(x)

print(s)