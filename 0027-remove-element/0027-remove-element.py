class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
         k = 0  # Initialize the pointer for the next valid position
    
         for i in range(len(nums)):  # Iterate through the array
           if nums[i] != val:  # Check if the element is not the target value
              nums[k] = nums[i]  # Move the current element to the position of k
              k += 1  # Increment k for the next valid element
            
         return k  # The length of the new array
