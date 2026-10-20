"""LeetCode 347: Top K Frequent Elements (Medium).

Given integer array nums and integer k, return the k most frequent elements.
You may return the answer in any order. The answer is guaranteed to be unique.
Aim for a time complexity better than O(n log n), where n = len(nums).

Examples: nums = [1, 1, 1, 2, 2, 3], k = 2 -> [1, 2];
nums = [1], k = 1 -> [1].
Constraints: 1 <= len(nums) <= 100000; -10000 <= nums[i] <= 10000;
1 <= k <= the number of unique elements.

Implement the blank method(s) below. No solution or algorithm hints included.
Run: python 05_top_k_frequent_elements.py
Uses only Python's standard library. Tests fail until you implement the solution.
"""

import unittest


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # TODO: Your solution goes here.








        pass


class TestTopKFrequentElements(unittest.TestCase):
    def test_cases(self):
        cases = [
            ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
            ([1], 1, [1]),
            ([4, 4, 4, 4], 1, [4]),
            ([-1, -1, 0, 0, 0, 2], 2, [0, -1]),
            ([1, 2, 3], 3, [1, 2, 3]),
            ([1, 1, 2, 2, 3], 2, [1, 2]),
            ([4, 1, -1, 2, -1, 2, 3], 2, [-1, 2]),
            ([-10000, -10000, 10000], 1, [-10000]),
            ([7] * 60000 + [8] * 30000 + [9] * 10000, 2, [7, 8]),
        ]
        for index, (nums, k, expected) in enumerate(cases):
            with self.subTest(case=index):
                actual = Solution().topKFrequent(nums, k)
                self.assertIsInstance(actual, list)
                self.assertCountEqual(actual, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
