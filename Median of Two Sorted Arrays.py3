class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = nums1 + nums2
        num.sort()
        n = len(num)

        mid = n // 2

        if n % 2 == 1:
            return num[mid]

        else:
            return (num[mid - 1] + num[mid]) / 2   
