from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for word in strs:
            # Counter("eat") -> {'e': 1, 'a': 1, 't': 1}
            # Convert items into a sorted tuple of (char, count) pairs so it is hashable
            key = tuple(sorted(Counter(word).items()))
            result[key].append(word)

        return list(result.values())