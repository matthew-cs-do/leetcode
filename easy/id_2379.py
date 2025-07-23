"""
    https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks
"""


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        b = 0
        for i in range(k):
            b += int(blocks[i] == 'B')
        if b == k:
            return 0
        m = b
        for i in range(k, len(blocks)):
            b = b - int(blocks[i - k] == 'B') + int(blocks[i] == 'B')
            if b == k:
                return 0
            elif b > m:
                m = b
        return k - m
