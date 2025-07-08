class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_count = 0
        for i in range(0, len(nums)):
            if nums[i] == 1:
                count += 1
                
            else:
                max_count = max(max_count,count)
                count = 0
        return max(max_count,count)



        #  count = 0       # Current streak of 1s
        # max_count = 0   # Max streak found so far

        # for num in nums:
        #     if num == 1:
        #         count += 1
        #         max_count = max(max_count, count)  # Update max streak
        #     else:
        #         count = 0  # Reset streak on 0

        # return max_count