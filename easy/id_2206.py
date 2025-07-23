"""
    https://leetcode.com/problems/divide-array-into-equal-pairs
"""
from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        mask = 0
        for num in nums:
            mask ^= 1 << num
        return mask == 0
