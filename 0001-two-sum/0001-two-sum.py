class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexed_nums = [(num, idx) for idx, num in enumerate(nums)]

        indexed_nums.sort()

        left = 0
        right = len(indexed_nums) - 1

        while left < right:
            left_val, left_idx = indexed_nums[left]
            right_val, right_idx = indexed_nums[right]
            cur_sum = left_val + right_val

            if cur_sum == target:
                return [left_idx, right_idx]
            elif cur_sum < target:
                left += 1
            else:
                right -= 1


        
        