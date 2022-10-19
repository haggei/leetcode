# https://leetcode.com/problems/container-with-most-water

from typing import List
import pytest


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        result = self.calc_area(height, left, right)

        while left < right:
            if height[left] < height[right]:
                last_height = height[left]
                while height[left] <= last_height and left < right:
                    left += 1
            else:
                last_height = height[right]
                while height[right] <= last_height and left < right:
                    right -= 1
            result = max(result, self.calc_area(height, left, right))
        return result

    def calc_area(self, height, a, b):
        width = b - a
        min_height = min(height[a], height[b])
        return width * min_height


@pytest.mark.parametrize(
    "nums,expected", [([1, 8, 6, 2, 5, 4, 8, 3, 7], 49), ([1, 1], 1)],
)
def test_max_area(nums, expected):
    assert expected == Solution().maxArea(nums)
