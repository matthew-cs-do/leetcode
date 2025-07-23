"""
    https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer
"""
from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = neg = 0
        while neg < len(nums) and nums[neg] < 0:
            neg += 1
        pos = neg
        while pos < len(nums) and nums[pos] == 0:
            pos += 1
        return max(neg, len(nums) - pos)
