"""LeetCode 3: Longest Substring Without Repeating Characters.

Given a string s, return the length of its longest contiguous substring
whose characters are all different. Return a length, not the substring.

Examples:
    "abcabcbb" -> 3
    "bbbbb"   -> 1
    "pwwkew"  -> 3 ("wke"; "pwke" is not contiguous)

Constraints:
    0 <= len(s) <= 100_000
    s can contain English letters, digits, symbols, and spaces.

Practice:
    1. Implement Solution.lengthOfLongestSubstring below.
    2. Run: python longest_substring.py
    3. All tests should pass once your implementation is correct.

The unfinished starter intentionally raises NotImplementedError.
No third-party packages are needed.
"""

import unittest


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Return the longest length with no repeated characters."""
        # Write your solution here.
        raise NotImplementedError("Implement lengthOfLongestSubstring first.")


class TestLongestSubstring(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_official_examples(self):
        for s, expected in [("abcabcbb", 3), ("bbbbb", 1), ("pwwkew", 3)]:
            with self.subTest(s=s):
                self.assertEqual(self.solution.lengthOfLongestSubstring(s), expected)

    def test_empty_string(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring(""), 0)

    def test_single_character(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("a"), 1)

    def test_all_unique(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("abcdef"), 6)

    def test_repeat_outside_current_substring(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("abba"), 2)

    def test_overlapping_repeats(self):
        for s, expected in [("dvdf", 3), ("tmmzuxt", 5), ("anviaj", 5)]:
            with self.subTest(s=s):
                self.assertEqual(self.solution.lengthOfLongestSubstring(s), expected)

    def test_longest_at_beginning_middle_or_end(self):
        for s, expected in [("abcdddd", 4), ("aaabcdefggg", 7), ("aaaaabcde", 5)]:
            with self.subTest(s=s):
                self.assertEqual(self.solution.lengthOfLongestSubstring(s), expected)

    def test_spaces_are_characters(self):
        for s, expected in [("     ", 1), ("a b c", 3)]:
            with self.subTest(s=s):
                self.assertEqual(self.solution.lengthOfLongestSubstring(s), expected)

    def test_digits_and_symbols(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("12!@12"), 4)

    def test_case_sensitive(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("aAbBcCa"), 6)

    def test_multiple_calls_on_same_solution(self):
        for s, expected in [("abc", 3), ("a", 1), ("", 0), ("ab", 2)]:
            with self.subTest(s=s):
                self.assertEqual(self.solution.lengthOfLongestSubstring(s), expected)

    def test_maximum_length_repeated_string(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("a" * 100_000), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
