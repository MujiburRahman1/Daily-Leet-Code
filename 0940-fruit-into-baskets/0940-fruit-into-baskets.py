from typing import List
from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0  # Window ka start
        max_fruits = 0  # Answer store karega
        fruit_count = defaultdict(int)  # Har fruit ka count

        for right in range(len(fruits)):
            fruit_count[fruits[right]] += 1  # Right fruit add karo

            # Agar basket mein 2 se zyada fruits hain, to window chhoti karo
            while len(fruit_count) > 2:
                fruit_count[fruits[left]] -= 1  # Left fruit hatao
                if fruit_count[fruits[left]] == 0:
                    del fruit_count[fruits[left]]  # Count 0 ho gaya to hata do
                left += 1  # Window ka left side agay karo

            # Max window size (maximum fruits)
            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits
