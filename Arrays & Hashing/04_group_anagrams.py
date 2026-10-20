"""LeetCode 49: Group Anagrams (Medium).

Given a list of strings strs, group the anagrams together.
Anagrams contain the same characters with the same frequencies.
Return a list of groups. Group order and order within each group do not matter.
Keep duplicates and empty strings.

Example: ["eat", "tea", "tan", "ate", "nat", "bat"]
    -> [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]].
Constraints: 1 <= len(strs) <= 10000; 0 <= len(strs[i]) <= 100;
lowercase English letters only.

Implement the blank method(s) below. No solution or algorithm hints included.
Run: python 04_group_anagrams.py
Uses only Python's standard library. Tests fail until you implement the solution.
"""

import unittest


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # TODO: Your solution goes here.








        pass


class TestGroupAnagrams(unittest.TestCase):
    def test_cases(self):
        cases = [
            (["eat", "tea", "tan", "ate", "nat", "bat"],
             [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]),
            ([""], [[""]]),
            (["a"], [["a"]]),
            (["", "", "a"], [["", ""], ["a"]]),
            (["ab", "ba", "ab"], [["ab", "ba", "ab"]]),
            (["a", "b", "c"], [["a"], ["b"], ["c"]]),
            (["abb", "aab", "bba", "aba"], [["abb", "bba"], ["aab", "aba"]]),
            (["abc"] * 10000, [["abc"] * 10000]),
        ]
        for index, (strs, expected) in enumerate(cases):
            with self.subTest(case=index):
                actual = Solution().groupAnagrams(strs)
                self.assertIsInstance(actual, list)
                for group in actual:
                    self.assertIsInstance(group, list)
                self.assertEqual(
                    sorted(tuple(sorted(group)) for group in actual),
                    sorted(tuple(sorted(group)) for group in expected),
                )


if __name__ == "__main__":
    unittest.main(verbosity=2)
