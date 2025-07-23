"""
    https://leetcode.com/problems/maximum-erasure-value
"""
from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        r = s = res = 0
        n = len(nums)
        for l in range(n):
            while r < n and nums[r] not in seen:
                s += nums[r]
                seen.add(nums[r])
                r += 1
                if s > res:
                    res = s
                if r == n:
                    return res
            s -= nums[l]
            seen.remove(nums[l])
        return res
