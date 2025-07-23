"""
    https://leetcode.com/problems/find-missing-and-repeated-values
"""
from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        s = 0
        n = len(grid)
        present = set()
        for i in range(n):
            for j in range(n):
                s += grid[i][j]
                if grid[i][j] in present:
                    a = grid[i][j]
                else:
                    present.add(grid[i][j])
        b = int(a - (s - (n ** 2 + 1) * n ** 2 / 2))
        return [a, b]
