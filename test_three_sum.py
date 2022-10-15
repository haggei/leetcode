# https://leetcode.com/problems/3sum/
import pytest
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        valid_three_sums = set()
        for a in range(len(nums)):
            for b in range(a + 1, len(nums)):
                for c in range(b + 1, len(nums)):
                    if nums[a] + nums[b] + nums[c] == 0:
                        zero_sum = [nums[a], nums[b], nums[c]]
                        zero_sum.sort()
                        valid_three_sums.add(tuple(zero_sum))
        return list(list(zero_sum) for zero_sum in valid_three_sums)


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
    ],
)
def test_three_sum(nums, expected):
    sol = Solution()
    result = sol.threeSum(nums)
    assert result == expected
