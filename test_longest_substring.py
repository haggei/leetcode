# https://leetcode.com/problems/longest-substring-without-repeating-characters/


import pytest


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring = 0
        current_letters = []
        for char in s:
            if char in current_letters:
                char_index = current_letters.index(char)
                current_letters = current_letters[char_index + 1 :]
            current_letters.append(char)
            longest_substring = max(longest_substring, len(current_letters))
        return longest_substring


@pytest.mark.parametrize(
    "s,expected", [("abcabcbb", 3), ("bbbbb", 1), ("pwwkew", 3)],
)
def test_topKFrequent(s, expected):
    sol = Solution()
    assert expected == sol.lengthOfLongestSubstring(s)
