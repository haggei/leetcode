# https://leetcode.com/problems/contains-duplicate/

from typing import List
import pytest


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
    ],
)
def test_containsDuplicate(nums, expected):
    assert expected == Solution().containsDuplicate(nums)
