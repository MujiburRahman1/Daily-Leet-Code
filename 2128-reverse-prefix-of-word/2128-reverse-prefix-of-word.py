class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = word.find(ch)  # Step 1: Find index of ch
        if idx == -1:
            return word       # Step 2: ch not found
        return word[:idx+1][::-1] + word[idx+1:]  # Step 3: Reverse prefix + rest
