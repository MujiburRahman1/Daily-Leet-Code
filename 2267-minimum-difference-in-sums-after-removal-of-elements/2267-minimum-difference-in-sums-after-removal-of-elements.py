import heapq

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        k = n // 3

        # Step 1: Build prefix sums using max-heap (simulated with min-heap by storing negatives)
        max_heap = []
        prefix = [0] * n
        total = 0

        # Process first k elements
        for i in range(k):
            heapq.heappush(max_heap, -nums[i])
            total += nums[i]
        prefix[k-1] = total

        # Process more elements and keep only k smallest
        for i in range(k, 2 * k):
            if -max_heap[0] > nums[i]:
                prefix[i] = prefix[i-1] + max_heap[0] + nums[i]  # max_heap[0] is negative
                heapq.heappop(max_heap)
                heapq.heappush(max_heap, -nums[i])
            else:
                prefix[i] = prefix[i-1]  # carry forward previous sum

        # Step 2: Build suffix sums using min-heap
        min_heap = []
        total = 0
        suffix = [0] * n

        # Process last k elements
        for i in range(n-1, n-k-1, -1):
            heapq.heappush(min_heap, nums[i])
            total += nums[i]
        suffix[n-k] = total

        # Process more elements and keep only k largest
        for i in range(n-k-1, k-1, -1):
            if min_heap[0] < nums[i]:
                suffix[i] = suffix[i+1] - min_heap[0] + nums[i]
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, nums[i])
            else:
                suffix[i] = suffix[i+1]  # carry forward previous sum

        # Step 3: Compute minimum difference between partitions
        min_diff = float('inf')
        for i in range(k-1, 2*k):
            min_diff = min(min_diff, prefix[i] - suffix[i+1])

        return min_diff