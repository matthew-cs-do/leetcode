"""
    https://leetcode.com/problems/maximum-matching-of-players-with-trainers
"""
from typing import List


class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        res = 0
        for i in range(len(trainers)):
            if players[res] <= trainers[i]:
                res += 1
            if res >= len(players):
                break
        return res
