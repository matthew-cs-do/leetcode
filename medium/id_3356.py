"""
    https://leetcode.com/problems/zero-array-transformation-ii
"""
from typing import List


class Solution:
    def compare(self, nums, pfx_sum):
        equal = True
        for i in range(len(nums)):
            if i > 0:
                pfx_sum[i] += pfx_sum[i-1]
            if nums[i] > pfx_sum[i]:
                return -1
            elif nums[i] < pfx_sum[i]:
                equal = False
        if equal:
            return 0
        return 1

    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        l = 0
        r = len(queries)
        while l <= r:
            m = l + (r-l)//2
            print(l,m,r)
            pfx_sum = [0]*len(nums)
            for query in queries[:m]:
                pfx_sum[query[0]] += query[2]
                if query[1] < len(nums) - 1:
                    pfx_sum[query[1]+1] -= query[2]
            compare = self.compare(nums,pfx_sum)
            if compare == 0:
                return m
            elif compare == 1:
                r = m - 1
            else:
                if m == len(queries):
                    return -1
                l = m + 1
            print(l,m,r)
        return l
