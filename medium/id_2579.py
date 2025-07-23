"""
    https://leetcode.com/problems/count-total-number-of-colored-cells
"""


class Solution:
    def coloredCells(self, n: int) -> int:
        if n == 1:
            return 1
        return 2*n-1+2*(n-1)**2
