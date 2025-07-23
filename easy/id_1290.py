"""
    https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        res = 0
        while head:
            res = res * 2 + head.val
            head = head.next
        return res
