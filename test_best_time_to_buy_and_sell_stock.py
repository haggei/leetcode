# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


from typing import List
import pytest


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_buy = prices[0]
        max_profit = 0
        for price in prices:
            if price < current_buy:
                current_buy = price
            else:
                max_profit = max(max_profit, price - current_buy)
        return max_profit


@pytest.mark.parametrize(
    "nums,expected", [([7, 1, 5, 3, 6, 4], 5), ([7, 6, 4, 3, 1], 0)],
)
def test_max_profit(nums, expected):
    assert expected == Solution().maxProfit(nums)
