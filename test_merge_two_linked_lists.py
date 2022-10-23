# https://leetcode.com/problems/merge-two-sorted-lists/

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
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        first_node = None
        last_node = None
        node = None
        while list1 or list2:
            if not list2 or list1 and list1.val < list2.val:
                node = list1
                list1 = node.next
            else:
                node = list2
                list2 = node.next
            node.next = None
            print(first_node)

            if not first_node:
                first_node = node
            if last_node:
                last_node.next = node
            last_node = node
        return first_node


@pytest.mark.parametrize(
    "list1,list2,expected",
    [
        (
            ListNode(1, ListNode(2, ListNode(4))),
            ListNode(1, ListNode(3, ListNode(4))),
            ListNode(
                1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4)))))
            ),
        ),
        (None, None, None),
        (None, ListNode(0), ListNode(0)),
    ],
)
def test_merge_list(list1, list2, expected):
    sol = Solution().mergeTwoLists(list1, list2)
    assert str(expected) == str(sol)
