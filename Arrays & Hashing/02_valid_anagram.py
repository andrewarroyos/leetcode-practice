"""LeetCode 242: Valid Anagram (Easy).

Given strings s and t, return True if t is an anagram of s, otherwise False.
An anagram uses exactly the same characters with the same frequencies,
possibly in a different order.

Examples: "anagram", "nagaram" -> True; "rat", "car" -> False.
Constraints: 1 <= len(s), len(t) <= 50000; lowercase English letters only.

Implement the blank method(s) below. No solution or algorithm hints included.
Run: python 02_valid_anagram.py
Uses only Python's standard library. Tests fail until you implement the solution.
"""

import unittest


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # TODO: Your solution goes here.








        pass


class TestValidAnagram(unittest.TestCase):
    def test_cases(self):
        cases = [
            ("anagram", "nagaram", True),
            ("rat", "car", False),
            ("a", "a", True),
            ("a", "b", False),
            ("ab", "a", False),
            ("aacc", "ccac", False),
            ("aab", "aba", True),
            ("abc", "abc", True),
            ("a" * 25000 + "b" * 25000, "b" * 25000 + "a" * 25000, True),
        ]
        for index, (s, t, expected) in enumerate(cases):
            with self.subTest(case=index):
                actual = Solution().isAnagram(s, t)
                self.assertIsInstance(actual, bool)
                self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
