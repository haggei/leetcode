import pytest
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)

        longest = 0
        current = 0
        for num in numbers:
            if num - 1 not in numbers:
                counter = num + 1
                current = 1
                while counter in numbers:
                    counter += 1
                    current += 1
                else:
                    longest = max(longest, current)
                    current = 0

        return longest


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
        ([], 0),
        ([0], 1),
    ],
)
def test_two_sum(nums, expected):
    assert expected == Solution().longestConsecutive(nums)
