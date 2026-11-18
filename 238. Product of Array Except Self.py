class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        results = [1] * n
        prefix = 1
        for i in range(n):
            results[i] = prefix
            prefix *= nums[i]

        sufix = 1
        for i in range(n-1, -1, -1):
            results[i] *= sufix
            sufix *= nums[i]
        
        return results 