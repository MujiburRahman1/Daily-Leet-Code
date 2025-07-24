class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n  # If k > n, wrap around (e.g., k=10 in 7-length array → k=3)

        def reverse(arr, start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1

        # Step 1: Reverse entire array
        reverse(nums, 0, n - 1)

        # Step 2: Reverse first k elements
        reverse(nums, 0, k - 1)

        # Step 3: Reverse remaining n-k elements
        reverse(nums, k, n - 1)
