from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        total_length = 0
        
        # Step 1: Count frequency of each character in chars
        chars_count = Counter(chars)

        # Step 2: Loop through each word in words list
        for word in words:
            word_count = Counter(word)  # Count characters in current word
            can_form = True

            # Step 3: Check if word can be formed from chars
            for c in word:
                if word_count[c] > chars_count.get(c, 0):
                    can_form = False
                    break
            
            # Step 4: If valid, add its length to total
            if can_form:
                total_length += len(word)

        return total_length
