# https://leetcode.com/problems/reverse-linked-list/

import pytest
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val}, {self.next}"


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        previous = None
        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
        return previous


@pytest.mark.parametrize(
    "head,expected",
    [
        (
            ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))),
            ListNode(5, ListNode(4, ListNode(3, ListNode(2, ListNode(1))))),
        ),
        (ListNode(1, ListNode(2)), ListNode(2, ListNode(1))),
    ],
)
def test_reverse_list(head, expected):
    sol = Solution().reverseList(head)
    assert str(expected) == str(sol)
