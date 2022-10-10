# https://leetcode.com/problems/two-sum/

from typing import List
import pytest


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previousNumbers = {}
        for i, val in enumerate(nums):
            if (target - val) in previousNumbers:
                return [previousNumbers[target - val], i]
            previousNumbers[val] = i


@pytest.mark.parametrize(
    "nums,target,expected",
    [([2, 7, 11, 15], 9, [0, 1]), ([3, 2, 4], 6, [1, 2]), ([3, 3], 6, [0, 1])],
)
def test_two_sum(nums, target, expected):
    sol = Solution()
    result = sol.twoSum(nums, target)
    assert result == expected

