class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        heshset = set(nums)
        longsub = 1
        for num in heshset:
            if (num - 1) in heshset:
                continue
            else:
                currentnum = num
                currentsub = 1
                while (currentnum + 1) in heshset:
                    currentnum += 1
                    currentsub += 1
                longsub = max(longsub, currentsub)
        
        return longsub