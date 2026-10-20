"""LeetCode 217: Contains Duplicate (Easy).

Given an integer array nums, return True if any value appears at least twice.
Return False if every element is distinct.

Examples: [1, 2, 3, 1] -> True; [1, 2, 3, 4] -> False.
Constraints: 1 <= len(nums) <= 100000; -10**9 <= nums[i] <= 10**9.

Implement the blank method(s) below. No solution or algorithm hints included.
Run: python 01_contains_duplicate.py
Uses only Python's standard library. Tests fail until you implement the solution.
"""

import unittest


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # TODO: Your solution goes here.








        pass


class TestContainsDuplicate(unittest.TestCase):
    def test_cases(self):
        cases = [
            ([1, 2, 3, 1], True),
            ([1, 2, 3, 4], False),
            ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
            ([1], False),
            ([0, 0], True),
            ([-1, 0, 1, -1], True),
            ([-10**9, 0, 10**9], False),
            (list(range(100000)), False),
            (list(range(99999)) + [0], True),
        ]
        for index, (nums, expected) in enumerate(cases):
            with self.subTest(case=index):
                actual = Solution().containsDuplicate(nums)
                self.assertIsInstance(actual, bool)
                self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
