# https://leetcode.com/problems/group-anagrams/

import pytest
from typing import List
from collections import Counter


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for word in strs:
            letters = frozenset(Counter(word).items())
            if letters in group:
                group[letters].append(word)
            else:
                group[letters] = [word]
        return list(group.values())


@pytest.mark.parametrize(
    "words,expected",
    [
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]],
        ),
        ([""], [[""]]),
        (["a"], [["a"]]),
        (["ddddddddddg", "dgggggggggg"], [["ddddddddddg"], ["dgggggggggg"]]),
    ],
)
def test_groupAnagrams(words, expected):
    sol = Solution()
    result = sol.groupAnagrams(words)
    assert result == expected
