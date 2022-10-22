# https://leetcode.com/problems/valid-parentheses/

import pytest


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {"(": ")", "[": "]", "{": "}"}
        for char in s:
            if char in parentheses:
                stack.append(parentheses[char])
            else:
                if stack and char == stack[-1]:
                    stack.pop()
                else:
                    return False
        return stack == []


@pytest.mark.parametrize(
    "s,expected", [("()", True), ("()[]{}", True), ("(]", False)],
)
def test_two_sum(s, expected):
    sol = Solution()
    result = sol.isValid(s)
    assert result == expected
