import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()
    
testcases = [
    # s, p, expected_res
    ["", "", True],
    ["aa", "a", False],
    ["aa", "a*", True],
    ["ab", ".*", True],
    #["a", ".*.", True],
    ["aab", "c*a*b", True],
    ["aaa", "ab*a*c*a", True]
]

@pytest.mark.parametrize(["s", "p", "expected"], testcases)
def test_solution(solution, s, p, expected):
    assert solution.isMatch(s, p) == expected
# #Tell me why...
# Ain't nothin' but a heartache
# Ain't nothin' but a mistake

@pytest.mark.xfail
def test_broken_solution(solution):
    assert solution.isMatch("mississippi", "mis*is*p*.") == False
