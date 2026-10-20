"""LeetCode 42: Trapping Rain Water (Hard).

Given nonnegative integer array height representing an elevation map,
where each bar has width 1, return the total water trapped after rain.
Water that can flow out through either end is not trapped.

Examples:
    [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1] -> 6
    [4, 2, 0, 3, 2, 5] -> 9

Constraints: 1 <= len(height) <= 20000; 0 <= height[i] <= 100000.

Implement the blank method below. No solution or algorithm hints included.
Run: python 05_trapping_rain_water.py
Uses only Python's standard library. Tests fail until you implement the solution.
"""

import unittest


class Solution:
    def trap(self, height: list[int]) -> int:
        # TODO: Your solution goes here.








        pass


class TestTrappingRainWater(unittest.TestCase):
    def test_cases(self):
        cases = [
            ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
            ([4, 2, 0, 3, 2, 5], 9),
            ([0], 0),
            ([5], 0),
            ([2, 1], 0),
            ([3, 3, 3], 0),
            ([1, 2, 3, 4], 0),
            ([4, 3, 2, 1], 0),
            ([3, 0, 3], 3),
            ([3, 0, 0, 3], 6),
            ([5, 0, 1], 1),
            ([1, 0, 5], 1),
            ([2, 0, 2, 0, 2], 4),
            ([0, 2, 0, 2, 0], 2),
            ([100000] + [0] * 19998 + [100000], 1999800000),
        ]
        for index, (height, expected) in enumerate(cases):
            with self.subTest(case=index):
                actual = Solution().trap(height)
                self.assertIsInstance(actual, int)
                self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
