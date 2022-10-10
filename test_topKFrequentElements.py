# https://leetcode.com/problems/top-k-frequent-elements/

from typing import List
import pytest


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            if num in counter.keys():
                counter[num] += 1
            else:
                counter[num] = 1

        rev_counter = {}
        for key, value in counter.items():
            if value in rev_counter:
                rev_counter[value] += [key]
            else:
                rev_counter[value] = [key]

        result = []
        while len(result) < k:
            key = max(rev_counter)
            result += rev_counter[key]
            rev_counter.pop(key)
        return result


@pytest.mark.parametrize(
    "nums,k,expected",
    [([1, 1, 1, 2, 2, 3], 2, [1, 2]), ([1], 1, [1]), ([-1, -1], 1, [-1])],
)
def test_topKFrequent(nums, k, expected):
    sol = Solution()
    assert expected == sol.topKFrequent(nums, k)
