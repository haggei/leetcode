# https://leetcode.com/problems/valid-anagram/

import pytest


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            print(len(s), len(t))
            return False
        for letter in s:
            if letter in t:
                t = t.replace(letter, "", 1)
            else:
                return False
        return True


@pytest.mark.parametrize(
    "s,t,result",
    [("anagram", "nagaram", True), ("rat", "car", False), ("aacc", "ccac", False)],
)
def test_is_anagram(s, t, result):
    sol = Solution()
    assert result == sol.isAnagram(s, t)
