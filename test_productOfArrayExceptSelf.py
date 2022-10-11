# https://leetcode.com/problems/product-of-array-except-self/

import pytest
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = self.listProduct(nums)
        result = []
        for i, num in enumerate(nums):
            if num == 0:
                rest_product = self.listProduct(nums[:i] + nums[i + 1 :])
                result.append(rest_product)
            else:
                result.append(product // num)
        return result

    def listProduct(self, nums: List[int]) -> int:
        product = 1
        for num in nums:
            product *= num
        return product


@pytest.mark.parametrize(
    "nums,expected",
    [([1, 2, 3, 4], [24, 12, 8, 6]), ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),],
)
def test_two_sum(nums, expected):
    assert expected == Solution().productExceptSelf(nums)
