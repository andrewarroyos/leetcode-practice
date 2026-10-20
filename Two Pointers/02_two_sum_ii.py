"""LeetCode 167: Two Sum II - Input Array Is Sorted (Medium).

Given a 1-indexed integer array numbers sorted in nondecreasing order,
find two numbers whose sum equals target.
Return their indices as [index1, index2], with index1 < index2.
The returned indices are ONE-BASED, not zero-based.
Exactly one valid pair exists. You cannot use the same element twice.
Your solution must use only constant extra space.

Examples:
    numbers = [2, 7, 11, 15], target = 9 -> [1, 2]
    numbers = [2, 3, 4], target = 6 -> [1, 3]
    numbers = [-1, 0], target = -1 -> [1, 2]

Constraints: 2 <= len(numbers) <= 30000;
-1000 <= numbers[i], target <= 1000.

Implement the blank method below. No solution or algorithm hints included.
Run: python 02_two_sum_ii.py
Uses only Python's standard library. Tests fail until you implement the solution.
"""

import unittest


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # TODO: Your solution goes here.








        pass


class TestTwoSumII(unittest.TestCase):
    def test_cases(self):
        cases = [
            ([2, 7, 11, 15], 9, [1, 2]),
            ([2, 3, 4], 6, [1, 3]),
            ([-1, 0], -1, [1, 2]),
            ([3, 3], 6, [1, 2]),
            ([0, 0, 3, 4], 0, [1, 2]),
            ([-5, -3, -1, 2], -8, [1, 2]),
            ([-10, -3, 0, 4, 9], 6, [2, 5]),
            ([1, 2, 4, 8], 12, [3, 4]),
            ([-1000, 0, 1000], 0, [1, 3]),
            ([-1] + [0] * 29998 + [2], 1, [1, 30000]),
        ]
        for index, (numbers, target, expected) in enumerate(cases):
            with self.subTest(case=index):
                actual = Solution().twoSum(numbers, target)
                self.assertIsInstance(actual, list)
                self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
