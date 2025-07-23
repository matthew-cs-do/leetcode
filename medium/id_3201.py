"""
    https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i
"""
from typing import List


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        odd_end_length = even_end_length = odd_only_length = even_only_length = 0
        for num in nums:
            if num % 2:
                odd_end_length = even_end_length + 1
                odd_only_length += 1
            else:
                even_end_length = odd_end_length + 1
                even_only_length += 1
        return max(odd_end_length, even_end_length, odd_only_length, even_only_length)
