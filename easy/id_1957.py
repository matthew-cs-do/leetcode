"""
    https://leetcode.com/problems/delete-characters-to-make-fancy-string
"""


class Solution:
    def makeFancyString(self, s: str) -> str:
        count = 0
        cur = s[0]
        res = ""
        for c in s:
            if c == cur:
                count += 1
            else:
                res += cur*min(count, 2)
                cur = c
                count = 1
        if count:
            res += cur*min(count, 2)
        return res
