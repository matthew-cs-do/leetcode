"""
    https://leetcode.com/problems/maximum-candies-allocated-to-k-children
"""
from typing import List


class Solution:
    def is_sufficient(self, candies, k, c):
        s = 0
        i = len(candies) - 1
        while i >= 0 and s < k:
            s += candies[i] // c
            if s >= k:
                return True
            i -= 1
        return False

    def maximumCandies(self, candies: List[int], k: int) -> int:
        l = 1
        r = max(candies)
        while l <= r:
            m = l + (r - l) // 2
            if self.is_sufficient(candies, k, m):
                l = m + 1
            else:
                r = m - 1
        return r
