class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for i in strs:
            sorted_i = ''.join(sorted(i))
            result[sorted_i].append(i)
        return list(result.values())