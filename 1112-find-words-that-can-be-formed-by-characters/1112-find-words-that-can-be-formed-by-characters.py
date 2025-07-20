from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_count = Counter(chars)
        total_length = 0

        for word in words:
            if Counter(word) <= chars_count:
                total_length += len(word)

        return total_length
