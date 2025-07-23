"""
    https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements
"""
from heapq import heappop, heappush
from typing import List


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3
        left_dp = [0] * (3*n)
        right_dp = [0] * (3*n)
        left_sum, right_sum = nums[0], nums[-1]
        left_dp[0] = nums[0]
        right_dp[3*n-1] = nums[-1]
        left_heap = [-nums[0]]
        right_heap = [nums[-1]]
        for i in range(1, 3*n):
            if len(left_heap) == n and left_heap[0] < - nums[i]:
                left_sum += heappop(left_heap)
            if len(left_heap) < n:
                heappush(left_heap, -nums[i])
                left_sum += nums[i]
            left_dp[i] = left_sum
            if len(right_heap) == n and right_heap[0] < nums[3*n-1-i]:
                right_sum -= heappop(right_heap)
            if len(right_heap) < n:
                heappush(right_heap, nums[3*n-1-i])
                right_sum += nums[3*n-1-i]
            right_dp[3*n-1-i] = right_sum
        res = left_dp[n-1] - right_dp[n]
        for i in range(n-1, 2*n):
            res = min(res, left_dp[i]-right_dp[i+1])
        return res
