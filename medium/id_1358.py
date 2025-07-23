"""
    https://leetcode.com/problems/number-of-substrings-containing-all-three-characters
"""


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = {}
        left = right = 0
        res = 0
        for left in range(len(s)):
            while not (len(count) == 3 or right >= len(s)):
                count[s[right]] = count.get(s[right], 0) + 1
                right += 1
            if len(count) == 3:
                res += len(s) - right + 1
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
            else:
                return res
