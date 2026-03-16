class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for word in strs:
            key = tuple(sorted(Counter(word).items()))
            anagram_map[key].append(word)

        return list(anagram_map.values())
        