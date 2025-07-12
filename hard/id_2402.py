"""
    https://leetcode.com/problems/meeting-rooms-iii/description
"""


from heapq import heappop, heappush
from typing import List


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        booked = []
        free = list(range(n))
        counter = [0] * n
        res = 0

        for start, end in meetings:
            while booked and booked[0][0] <= start:
                _, room = heappop(booked)
                heappush(free, room)

            if not free:
                actual_start, room = heappop(booked)
                end += actual_start - start
            else:
                room = heappop(free)

            heappush(booked, (end, room))
            counter[room] += 1

        for i in range(n):
            if counter[i] > counter[res]:
                res = i
        return res
