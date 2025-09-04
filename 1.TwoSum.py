from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        self.nums = nums
        self.target = target

        for x in range(len(nums)):
            for y in range(len(nums)):
                sum = nums[x] + nums[y]
                if sum == target and x != y:
                    sol = [x,y]

        return sol 

nums = [3,3]

target = 6

sol = Solution()
s = sol.twoSum(nums=nums, target=target)

print(s)