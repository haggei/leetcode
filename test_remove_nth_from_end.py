# https://leetcode.com/problems/reorder-list/


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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        length = 1
        while node.next:
            length += 1
            node = node.next

        node = head
        prev = None
        while length - n > 0:
            length -= 1
            prev = node
            node = node.next

        if not prev:
            head = head.next
        else:
            prev.next = node.next
        return head


@pytest.mark.parametrize(
    "head,n,expected",
    [
        (
            ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))),
            2,
            ListNode(1, ListNode(2, ListNode(3, ListNode(5)))),
        ),
        (ListNode(1), 1, None,),
        (ListNode(1, ListNode(2)), 1, ListNode(1)),
    ],
)
def test_merge_list(head, n, expected):
    result = Solution().removeNthFromEnd(head, n)
    assert str(expected) == str(result)
