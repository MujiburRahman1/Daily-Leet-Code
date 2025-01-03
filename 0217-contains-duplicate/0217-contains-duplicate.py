class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()  # Create an empty set to store numbers we've encountered
        for num in nums: # Iterate through each number in the list
            if num in seen: # If the already in the set 
                return True # We found a dupicate, so return True
            seen.add(num) # Otherwise add the number to the set
        return False # If no duplicates were found, return False