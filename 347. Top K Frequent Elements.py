class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hmap = Counter(nums)
        rank = dict(sorted(hmap.items(), key=lambda item: item[1], reverse=True))
        return list(rank.keys())[:k]


