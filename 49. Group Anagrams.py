class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        if len(strs) == 0:
            return []
        ansmap = {}
        for s in strs:
            count = [0] *26
            for i in range(len(s)):
                count[ord(s[i]) - ord('a')] += 1
            key = tuple(count)

            if key not in ansmap:
                ansmap[key] = []

            ansmap[key].append(s)

        return list(ansmap.values())
            
            