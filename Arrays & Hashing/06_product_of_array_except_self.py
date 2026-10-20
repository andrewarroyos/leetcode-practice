"""LeetCode 238: Product of Array Except Self (Medium).

Given integer array nums, return an array answer where answer[i] is the product
of every element of nums except nums[i].
Use O(n) time and do not use division.
Follow-up: use O(1) extra space, excluding the returned array.

Example: [1, 2, 3, 4] -> [24, 12, 8, 6].
Constraints: 2 <= len(nums) <= 100000; -30 <= nums[i] <= 30.
Prefix, suffix, and answer products fit in a signed 32-bit integer.

Implement the blank method(s) below. No solution or algorithm hints included.
Run: python 06_product_of_array_except_self.py
Uses only Python's standard library. Tests fail until you implement the solution.
"""

import unittest


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # TODO: Your solution goes here.








        pass


class TestProductExceptSelf(unittest.TestCase):
    def test_cases(self):
        cases = [
            ([1, 2, 3, 4], [24, 12, 8, 6]),
            ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
            ([2, 3], [3, 2]),
            ([0, 0], [0, 0]),
            ([0, 2, 3], [6, 0, 0]),
            ([2, 3, 0], [0, 0, 6]),
            ([0, 2, 0, 4], [0, 0, 0, 0]),
            ([-1, -2, -3, -4], [-24, -12, -8, -6]),
            ([1, 1, 1], [1, 1, 1]),
            ([1] * 100000, [1] * 100000),
        ]
        for index, (nums, expected) in enumerate(cases):
            with self.subTest(case=index):
                self.assertEqual(Solution().productExceptSelf(nums), expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
