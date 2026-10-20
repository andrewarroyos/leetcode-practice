"""LeetCode 4: Median of Two Sorted Arrays (Hard).

Given two sorted integer arrays nums1 and nums2 of lengths m and n,
return the median of all their elements combined.

Required overall time complexity: O(log(m + n)).

Examples:
    nums1 = [1, 3], nums2 = [2]     -> 2.0
    nums1 = [1, 2], nums2 = [3, 4]  -> 2.5

Constraints:
    0 <= m, n <= 1000
    1 <= m + n <= 2000
    -10**6 <= nums1[i], nums2[i] <= 10**6
    Both input arrays are sorted in nondecreasing order.

Implement only Solution.findMedianSortedArrays below.
Run tests: python median_of_two_sorted_arrays.py
No third-party packages required. Tests fail until you implement the solution.
"""

import unittest


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # TODO: Write your solution here.
        """
        I had to look up the solution. I struggled here for sure.
        """
        
        m = len(nums1)
        n = len(nums2)
        total = m + n

        # Indices into each array.
        p1 = 0
        p2 = 0

        previous = 0
        current = 0

        # Visit elements through the middle position.
        for _ in range(total // 2 + 1):
            previous = current

            if p1 < m and (p2 >= n or nums1[p1] <= nums2[p2]):
                current = nums1[p1]
                p1 += 1
            else:
                current = nums2[p2]
                p2 += 1

        if total % 2 == 1:
            return float(current)

        return (previous + current) / 2

        pass


class TestMedianOfTwoSortedArrays(unittest.TestCase):
    def test_medians(self):
        cases = [
            ("example_1", [1, 3], [2], 2.0),
            ("example_2", [1, 2], [3, 4], 2.5),
            ("empty_first", [], [1], 1.0),
            ("empty_second", [2], [], 2.0),
            ("empty_first_even", [], [1, 2, 3, 4], 2.5),
            ("empty_second_odd", [1, 2, 3], [], 2.0),
            ("one_element_each", [1], [2], 1.5),
            ("all_zeros", [0, 0], [0, 0], 0.0),
            ("duplicates", [1, 1], [1, 2], 1.0),
            ("negative_only", [-5, -3, -1], [-4, -2], -3.0),
            ("negative_fraction", [-3], [-2], -2.5),
            ("mixed_signs", [-5, -1, 3], [-2, 4, 6], 1.0),
            ("nonoverlapping", [1, 2, 3], [10, 11, 12], 6.5),
            ("reverse_nonoverlapping", [10, 11], [1, 2, 3], 3.0),
            ("unequal_lengths", [100], [1, 2, 3, 4, 5, 6], 4.0),
            ("unequal_lengths_swapped", [1, 2, 3, 4, 5, 6], [100], 4.0),
            ("value_limits", [-10**6], [10**6], 0.0),
            ("maximum_lengths", list(range(1000)), list(range(1000, 2000)), 999.5),
        ]

        for name, nums1, nums2, expected in cases:
            with self.subTest(case=name):
                actual = Solution().findMedianSortedArrays(nums1, nums2)
                self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)