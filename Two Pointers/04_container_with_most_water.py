"""LeetCode 11: Container With Most Water (Medium).

Given an integer array height, each index i represents a vertical line from
(i, 0) to (i, height[i]). Choose two lines that, together with the x-axis,
form a container holding the most water. Return its maximum area.
The area for lines i and j is (j - i) * min(height[i], height[j]).
You cannot tilt the container.

Examples:
    [1, 8, 6, 2, 5, 4, 8, 3, 7] -> 49
    [1, 1] -> 1

Constraints: 2 <= len(height) <= 100000; 0 <= height[i] <= 10000.

Implement the blank method below. No solution or algorithm hints included.
Run: python 04_container_with_most_water.py
Uses only Python's standard library. Tests fail until you implement the solution.
"""

import unittest


class Solution:
    def maxArea(self, height: list[int]) -> int:
        # TODO: Your solution goes here.








        pass


class TestContainerWithMostWater(unittest.TestCase):
    def test_cases(self):
        cases = [
            ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
            ([1, 1], 1),
            ([0, 0], 0),
            ([0, 5], 0),
            ([5, 5, 5, 5], 15),
            ([1, 2, 3, 4, 5], 6),
            ([5, 4, 3, 2, 1], 6),
            ([4, 3, 2, 1, 4], 16),
            ([1, 100, 100, 1], 100),
            ([10, 0, 0, 0, 10], 40),
            ([10000] * 100000, 999990000),
        ]
        for index, (height, expected) in enumerate(cases):
            with self.subTest(case=index):
                actual = Solution().maxArea(height)
                self.assertIsInstance(actual, int)
                self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
