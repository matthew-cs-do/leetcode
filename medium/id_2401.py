"""
    https://leetcode.com/problems/longest-nice-subarray
"""
from typing import List


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        l = r = 0
        s = 0
        res = 0
        while l < len(nums) and r < len(nums):
            if s & nums[r] == 0:
                s |= nums[r]
                r += 1
                res = max(res, r-l)
                if res == 30:
                    break
            else:
                s -= nums[l]
                l += 1
        return res
