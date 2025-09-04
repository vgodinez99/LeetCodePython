class Solution:
    def romanToInt(self, s: str) -> int:
        
        self.s = s

        dic = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,}
        sum = 0

        for i in range(len(s)):
            if s[i] == "I":
                if s[i+1] = "V":
                    

            sum = sum + dic[s[i]]

        return sum
    
s = 'MCMXCIV'

sol = Solution()
s = sol.romanToInt(s)

print(s)