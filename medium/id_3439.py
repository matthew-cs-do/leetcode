"""
    https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/description/
"""


from typing import List


class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        gaps = []
        cur_end = 0
        for start, end in zip(startTime, endTime):
            gaps.append(start-cur_end)
            cur_end = end
        gaps.append(eventTime-cur_end)
        gaps_count = len(gaps)
        res = cur = sum(gaps[:k+1])
        for i in range(0, gaps_count-k-1):
            cur = cur - gaps[i] + gaps[i+k+1]
            res = max(res, cur)
        return res
