"""LeetCode 15: 3Sum (Medium).

Given an integer array nums, return all unique triplets [nums[i], nums[j], nums[k]]
whose sum is zero, where i, j, and k are distinct indices.
The answer must not contain duplicate triplets.
You may return triplets and their elements in any order.

Examples:
    [-1, 0, 1, 2, -1, -4] -> [[-1, -1, 2], [-1, 0, 1]]
    [0, 1, 1] -> []
    [0, 0, 0] -> [[0, 0, 0]]

Constraints: 3 <= len(nums) <= 3000; -100000 <= nums[i] <= 100000.

Implement the blank method below. No solution or algorithm hints included.
Run: python 03_three_sum.py
Uses only Python's standard library. Tests fail until you implement the solution.
"""

import unittest


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # TODO: Your solution goes here.








        pass


class TestThreeSum(unittest.TestCase):
    def test_cases(self):
        cases = [
            ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
            ([0, 1, 1], []),
            ([0, 0, 0], [[0, 0, 0]]),
            ([0, 0, 0, 0], [[0, 0, 0]]),
            ([1, 2, 3], []),
            ([-3, -2, -1], []),
            ([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]]),
            ([-2, -2, 0, 0, 2, 2], [[-2, 0, 2]]),
            ([-4, -2, -2, 0, 2, 4],
             [[-4, 0, 4], [-2, -2, 4], [-2, 0, 2]]),
            ([-100000, 0, 100000], [[-100000, 0, 100000]]),
            ([0] * 3000, [[0, 0, 0]]),
        ]
        for index, (nums, expected) in enumerate(cases):
            with self.subTest(case=index):
                actual = Solution().threeSum(nums)
                self.assertIsInstance(actual, list)
                for triplet in actual:
                    self.assertIsInstance(triplet, list)
                    self.assertEqual(len(triplet), 3)
                # Sorting preserves duplicate triplets, so duplicates fail too.
                self.assertEqual(
                    sorted(tuple(sorted(triplet)) for triplet in actual),
                    sorted(tuple(sorted(triplet)) for triplet in expected),
                )


if __name__ == "__main__":
    unittest.main(verbosity=2)
