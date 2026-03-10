class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num = len(nums)
    
        for i in range(num):
            for j in range(i + 1, num):
                if nums[i] + nums[j] == target:
                    return [i, j]
