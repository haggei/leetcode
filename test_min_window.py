# https://leetcode.com/problems/minimum-window-substring/

import pytest
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_window = None
        letter_count = Counter(t)
        current_window_count = {}
        current_window = ""
        for i, char in enumerate(s):
            current_window += char
            if char in current_window_count:
                current_window_count[char] += 1
            else:
                current_window_count[char] = 1
            while self.is_valid_window(current_window_count, letter_count):
                if not min_window or len(min_window) > len(current_window):
                    min_window = current_window
                current_window_count[current_window[0]] -= 1
                current_window = current_window[1:]
        return min_window or ""

    def is_valid_window(self, current_window_count, letter_count):
        for key in letter_count:
            if (
                key not in current_window_count
                or current_window_count[key] < letter_count[key]
            ):
                return False
        return True


@pytest.mark.parametrize(
    "s,t,expected",
    [("ADOBECODEBANC", "ABC", "BANC"), ("a", "a", "a"), ("a", "aa", "")],
)
def test_topKFrequent(s, t, expected):
    sol = Solution()
    assert expected == sol.minWindow(s, t)
