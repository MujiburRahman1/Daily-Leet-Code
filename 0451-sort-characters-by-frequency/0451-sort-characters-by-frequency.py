class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)

        sorted_chars = sorted(freq, key = lambda c: freq[c], reverse = True)

        result = "".join(char * freq[char] for char in sorted_chars)

        return result