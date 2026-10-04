"""Two Sum practice — Python 3.9+

Given a list of integers nums and an integer target, return the indices
of the two numbers that add up to target.

Rules:
    - Each input has exactly one valid pair.
    - You cannot use the same element twice.
    - Return indices, not values. Either index order is accepted.

Example: nums = [2, 7, 11, 15], target = 9 -> [0, 1]

Implement Solution.twoSum below, then run: python two_sum.py
No extra packages are required. Tests will fail until you implement it.
"""

import unittest


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Solution here
        hashmap = {}
        
        index = 0
        for num in nums:
          complement = target - num
          if complement in hashmap:
            return [hashmap[complement], index]
          hashmap[num] = index
          index += 1
          
          
        
        
        # --------------- Do not modify under --------------
        raise NotImplementedError("Implement twoSum to begin practicing.")


class TestTwoSum(unittest.TestCase):
    def test_cases(self):
        # Description, input numbers, target, expected indices
        cases = [
            ("basic example", [2, 7, 11, 15], 9, [0, 1]),
            ("pair after first element", [3, 2, 4], 6, [1, 2]),
            ("duplicate values", [3, 3], 6, [0, 1]),
            ("negative values", [-1, -2, -3, -4, -5], -8, [2, 4]),
            ("mixed signs", [-3, 4, 3, 90], 0, [0, 2]),
            ("two zeros", [0, 4, 3, 0], 0, [0, 3]),
            ("do not reuse an index", [3, 2, 4, 8], 6, [1, 2]),
            ("far apart indices", [5, 1, 8, 12, 20], 25, [0, 4]),
            ("large numbers", [1000000000, 7, -1000000000], 0, [0, 2]),
        ]

        for description, nums, target, expected in cases:
            with self.subTest(case=description, nums=nums, target=target):
                result = Solution().twoSum(nums.copy(), target)
                self.assertIsInstance(result, list, "Return a list of indices.")
                self.assertEqual(len(result), 2, "Return exactly two indices.")
                for index in result:
                    self.assertIs(type(index), int, "Each index must be an integer.")
                    self.assertTrue(0 <= index < len(nums), "Index is out of range.")
                self.assertNotEqual(result[0], result[1], "Use different indices.")
                self.assertEqual(sorted(result), sorted(expected))
                self.assertEqual(nums[result[0]] + nums[result[1]], target)


if __name__ == "__main__":
    unittest.main(verbosity=2)