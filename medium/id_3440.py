"""
    https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii/description/
"""

from typing import List


class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        gaps = []
        cur_end = 0
        gap_1 = i1 = gap_2 = i2 = gap_3 = i3 = 0
        for i, (start, end) in enumerate(zip(startTime, endTime)):
            gaps.append(start - cur_end)
            if gaps[-1] > gap_1:
                gap_1, i1, gap_2, i2, gap_3, i3 = gaps[-1], i, gap_1, i1, gap_2, i2
            elif gaps[-1] > gap_2:
                gap_2, i2, gap_3, i3 = gaps[-1], i, gap_2, i2
            elif gaps[-1] > gap_3:
                gap_3, i3 = gaps[-1], i
            cur_end = end
        gaps.append(eventTime - cur_end)
        if gaps[-1] > gap_1:
            gap_1, i1, gap_2, i2, gap_3, i3 = gaps[-1], n, gap_1, i1, gap_2, i2
        elif gaps[-1] > gap_2:
            gap_2, i2, gap_3, i3 = gaps[-1], n, gap_2, i2
        elif gaps[-1] > gap_3:
            gap_3, i3 = gaps[-1], n

        def is_movable(meet_index):
            meet_length = endTime[meet_index] - startTime[meet_index]
            if meet_length <= gap_1 and meet_index != i1 and meet_index != i1 - 1:
                return True
            if meet_length <= gap_2 and meet_index != i2 and meet_index != i2 - 1:
                return True
            if meet_length <= gap_3 and meet_index != i3 and meet_index != i3 - 1:
                return True
            return False

        res = 0
        for i in range(len(startTime)):
            extra = endTime[i] - startTime[i] if is_movable(i) else 0
            res = max(
                res,
                gaps[i] + gaps[i + 1] + extra
            )

        return res
