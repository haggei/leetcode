# https://leetcode.com/problems/longest-repeating-character-replacement/

import pytest


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        start = 0
        current_chars = {}
        for i, char in enumerate(s):
            if char in current_chars:
                current_chars[char] += 1
            else:
                current_chars[char] = 1
            while sum(current_chars.values()) - max(current_chars.values()) > k:
                current_chars[s[start]] -= 1
                start += 1
            max_length = max(max_length, sum(current_chars.values()))
        return max_length


@pytest.mark.parametrize(
    "s,k,expected", [("ABAB", 2, 4), ("AABABBA", 1, 4)],
)
def test_topKFrequent(s, k, expected):
    sol = Solution()
    assert expected == sol.characterReplacement(s, k)
