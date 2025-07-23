"""
    https://leetcode.com/problems/apply-operations-to-an-array
"""
from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        while i < n-1:
            if nums[i] == nums[i+1]:
                nums[i] = 0
                nums[i+1] *= 2
                i += 2
            else:
                i += 1
        return [i for i in nums if i != 0] + [0] * nums.count(0)
