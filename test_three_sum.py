# https://leetcode.com/problems/3sum/
import pytest
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        two_sum: dict[tuple[int, int], int] = {}
        for a in range(len(nums)):
            for b in range(a + 1, len(nums)):
                two_sum[(a, b)] = nums[a] + nums[b]

        result_indices = set()
        for c in range(len(nums)):
            for keys, val in two_sum.items():
                if c in keys:
                    continue
                if val + nums[c] == 0:
                    result_indices.add((keys[0], keys[1], c))

        result = set()

        for i in result_indices:
            zero_sum = [nums[i[0]], nums[i[1]], nums[i[2]]]
            zero_sum.sort()
            result.add(tuple(zero_sum))

        return [list(zero_sum) for zero_sum in result]


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([-1, 0, 1, 2, -1, -4], [[-1, 0, 1], [-1, -1, 2]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
    ],
)
def test_three_sum(nums, expected):
    sol = Solution()
    result = sol.threeSum(nums)
    assert result == expected
