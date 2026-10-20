"""LeetCode 128: Longest Consecutive Sequence (Medium).

Given an unsorted integer array nums, return the length of the longest sequence
of consecutive integer values present in the array.
The values do not need to appear next to each other or in order in the input.
Duplicates do not extend a sequence. Your algorithm must run in O(n) time.

Examples: [100, 4, 200, 1, 3, 2] -> 4 (values 1, 2, 3, 4);
[0, 3, 7, 2, 5, 8, 4, 6, 0, 1] -> 9.
Constraints: 0 <= len(nums) <= 100000; -10**9 <= nums[i] <= 10**9.

Implement the blank method(s) below. No solution or algorithm hints included.
Run: python 09_longest_consecutive_sequence.py
Uses only Python's standard library. Tests fail until you implement the solution.
"""

import unittest


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # TODO: Your solution goes here.








        pass


class TestLongestConsecutiveSequence(unittest.TestCase):
    def test_cases(self):
        cases = [
            ([100, 4, 200, 1, 3, 2], 4),
            ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
            ([], 0),
            ([42], 1),
            ([7, 7, 7], 1),
            ([1, 2, 0, 1], 3),
            ([-2, -3, -1, 1], 3),
            ([-1, 0, 1, 2], 4),
            ([10, 30, 50], 1),
            ([1, 2, 10, 11, 12], 3),
            ([-10**9, 10**9], 1),
            (list(range(99999, -1, -1)), 100000),
        ]
        for index, (nums, expected) in enumerate(cases):
            with self.subTest(case=index):
                actual = Solution().longestConsecutive(nums)
                self.assertIsInstance(actual, int)
                self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
