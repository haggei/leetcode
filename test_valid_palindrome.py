# https://leetcode.com/problems/valid-palindrome/

import pytest


class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = [letter for letter in s.lower() if letter.isalnum()]
        for i in range(len(cleaned_s)):
            if cleaned_s[i] != cleaned_s[-(i + 1)]:
                return False
        return True


@pytest.mark.parametrize(
    "s,expected",
    [("A man, a plan, a canal: Panama", True), ("race a car", False), (" ", True)],
)
def test_two_sum(s, expected):
    sol = Solution()
    result = sol.isPalindrome(s)
    assert result == expected
