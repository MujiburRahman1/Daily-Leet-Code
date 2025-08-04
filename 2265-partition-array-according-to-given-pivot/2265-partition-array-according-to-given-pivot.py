from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # Arrays to store elements less than, equal to, and greater than pivot
        less_than = []
        equal_to = []
        greater_than = []

        # Traverse the input array and partition elements
        for num in nums:
            if num < pivot:
                less_than.append(num)
            elif num == pivot:
                equal_to.append(num)
            else:
                greater_than.append(num)

        # Combine all parts while preserving relative order
        return less_than + equal_to + greater_than
