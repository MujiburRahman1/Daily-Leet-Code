class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)

        answer1 = 0
        for x in nums1:
            if x in set2:
                answer1 += 1
        
        answer2 = 0
        for x in nums2:
            if x in set1:
                answer2 += 1
        return [answer1, answer2]