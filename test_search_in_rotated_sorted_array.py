# https://leetcode.com/problems/search-in-rotated-sorted-array/


import pytest
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        return -1


@pytest.mark.parametrize(
    "nums, target ,expected",
    [([4, 5, 6, 7, 0, 1, 2], 0, 4), ([4, 5, 6, 7, 0, 1, 2], 3, -1), ([1], 0, -1)],
)
def test_two_sum(nums, target, expected):
    assert expected == Solution().search(nums, target)
