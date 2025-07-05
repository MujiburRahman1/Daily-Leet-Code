class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        #start form index 
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i - 1] #add previuos sum to current element
        return nums