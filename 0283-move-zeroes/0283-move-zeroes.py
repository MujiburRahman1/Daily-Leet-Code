class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0 
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left] = nums[right]
                left +=1
        while left < len(nums):
            nums[left] = 0
            left += 1