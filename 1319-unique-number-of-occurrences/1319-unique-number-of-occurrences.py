class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count_map = Counter(arr)

        frequencies = list(count_map.values())
        return len(frequencies) == len(set(frequencies))