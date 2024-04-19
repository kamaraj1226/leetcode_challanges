"""
##########################
# Solution By: Kamaraj J #
##########################
"""

# pylint: disable=use-dict-literal
# pylint: disable=too-few-public-methods
# pylint: disable=invalid-name

from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        



def run_test():
    """
    Test cases
    """
    test_cases = {
        1: dict(points=[[10, 16], [2, 8], [1, 6], [7, 12]], output=2),
        2: dict(points=[[1, 2], [3, 4], [5, 6], [7, 8]], output=4),
        3: dict(points=[[1, 2], [2, 3], [3, 4], [4, 5]], output=2),
    }

    for test_case in test_cases:
        points, output = test_cases.get(test_case).values()
        solution = Solution()
        final_output = solution.findMinArrowShots(points)
        if output == final_output:
            print(f"Test case: {test_case} Passed")
        else:
            print(f"Test case: {test_case} Failed")


if __name__ == "__main__":
    run_test()
