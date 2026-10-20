"""LeetCode 1: Two Sum (Easy).

Given integer array nums and integer target, return the indices of two elements
whose values add to target. You cannot use the same element twice.
Exactly one valid pair exists. Return the indices in either order.

Example: nums = [2, 7, 11, 15], target = 9 -> [0, 1].
Constraints: 2 <= len(nums) <= 10000;
-10**9 <= nums[i], target <= 10**9.

Implement the blank method(s) below. No solution or algorithm hints included.
Run: python 03_two_sum.py
Uses only Python's standard library. Tests fail until you implement the solution.
"""

import unittest


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # TODO: Your solution goes here.








        pass


class TestTwoSum(unittest.TestCase):
    def test_cases(self):
        cases = [
            ([2, 7, 11, 15], 9, [0, 1]),
            ([3, 2, 4], 6, [1, 2]),
            ([3, 3], 6, [0, 1]),
            ([-3, 4, 3, 90], 0, [0, 2]),
            ([0, 4, 3, 0], 0, [0, 3]),
            ([1, 2, 3, 4], 7, [2, 3]),
            ([-1, -2, -3, -4, -5], -8, [2, 4]),
            ([-10**9, 10**9], 0, [0, 1]),
            (list(range(10000)), 19997, [9998, 9999]),
        ]
        for index, (nums, target, expected) in enumerate(cases):
            with self.subTest(case=index):
                actual = Solution().twoSum(nums, target)
                self.assertIsInstance(actual, list)
                self.assertCountEqual(actual, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
