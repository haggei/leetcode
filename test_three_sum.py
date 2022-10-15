# https://leetcode.com/problems/3sum/
import pytest
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        valid_three_sums = set()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            left = 0
            right = len(nums) - 1
            while right > left:
                while a + nums[left] + nums[right] > 0 or right == i:
                    right -= 1
                    if right <= left:
                        break
                while a + nums[left] + nums[right] < 0 or left == i:
                    left += 1
                    if left >= right:
                        break
                if left == right or i == left or i == right:
                    continue
                if a + nums[left] + nums[right] == 0:
                    zero_sum = [a, nums[left], nums[right]]
                    zero_sum.sort()
                    valid_three_sums.add(tuple(zero_sum))
                    left += 1

        return list(list(zero_sum) for zero_sum in valid_three_sums)


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([-1, 0, 1, 2, -1, -4], [[-1, 0, 1], [-1, -1, 2]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
        ([-2, 1, 4], []),
    ],
)
def test_three_sum(nums, expected):
    sol = Solution()
    result = sol.threeSum(nums)
    assert result == expected
