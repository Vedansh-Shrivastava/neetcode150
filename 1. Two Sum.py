class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashm = {}
        for i in range(len(nums)):
            compliment = target - nums[i]

            if compliment in hashm:
                return [hashm[compliment], i]
            
            hashm[nums[i]] = i
            