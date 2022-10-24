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
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Reverse Linked list and count elements
        reverse_head = ListNode(head.val)
        node = head
        counter = 0
        while node.next:
            counter += 1
            reverse_head = ListNode(node.next.val, reverse_head)
            node = node.next

        # Join linked list mit reversed linked list
        node = head
        while node.next:
            temp1 = node.next
            temp2 = reverse_head.next
            node.next = reverse_head
            reverse_head.next = temp1
            reverse_head = temp2
            node = node.next.next

        # Take first half of the linked list
        node = head
        while counter > 0:
            node = node.next
            counter -= 1
        node.next = None


@pytest.mark.parametrize(
    "head,expected",
    [
        (
            ListNode(1, ListNode(2, ListNode(3, ListNode(4)))),
            ListNode(1, ListNode(4, ListNode(2, ListNode(3)))),
        ),
        (
            ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))),
            ListNode(1, ListNode(5, ListNode(2, ListNode(4, ListNode(3))))),
        ),
    ],
)
def test_merge_list(head, expected):
    Solution().reorderList(head)
    assert str(expected) == str(head)
