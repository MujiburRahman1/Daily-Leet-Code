class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        #   HASH SET
        # num1Set, num2Set = set(nums1), set(nums2)
        # res1, res2 = [], []

        # for num in num1Set:
        #     if num not in num2Set:
        #         res1.append(num)

        # for num in num2Set:
        #     if num not in num1Set:
        #         res2.append(num)
        
        # return [res1, res2]

        # BRUTE FORCE
        # res = [set(), set()]
        # for num1 in nums1:
        #     if num1 not in nums2:
        #         res[0].add(num1)

        # for num2 in nums2:
        #     if num2 not in nums1:
        #         res[1].add(num2)

        # return [list(res[0]), list(res[1])]


        # HASH SET DIFFERNCE
        set1 = set(nums1)
        set2 = set(nums2)

        res1 = list(set1 - set2)
        res2 = list(set2 - set1)

        return [res1, res2]