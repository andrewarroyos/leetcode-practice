"""Encode and Decode Strings (Medium; LeetCode 271).

Design a codec to encode a list of strings into one string and decode that
string back into the original list. Preserve order, duplicates, and empty strings.
There is no required encoding format; any unambiguous, reversible format works.
Do not use serialization helpers such as json or pickle as the solution.

Implement Codec.encode(strs) -> str and Codec.decode(s) -> list[str].
The decoder must work on a fresh Codec instance without access to the input list.

Example: ["hello", "world"] -> encoded string -> ["hello", "world"].
Practice inputs include an empty list, empty strings, punctuation, whitespace,
and Unicode. These broaden the usual platform character constraints.

Implement the blank method(s) below. No solution or algorithm hints included.
Run: python 08_encode_and_decode_strings.py
Uses only Python's standard library. Tests fail until you implement the solution.
"""

import unittest


class Codec:
    def encode(self, strs: list[str]) -> str:
        # TODO: Encode the list into one string.






        pass

    def decode(self, s: str) -> list[str]:
        # TODO: Decode the string back into the original list.






        pass


class TestEncodeDecodeStrings(unittest.TestCase):
    def test_round_trips(self):
        cases = [
            [],
            [""],
            ["", "", ""],
            ["hello", "world"],
            ["neet", "code", "love", "you"],
            ["a", "a", "b"],
            ["", "hello", "", "world", ""],
            ["#", "##", "3#abc", "12:hello", ":"],
            ["a b", "line1\nline2", "\t", "\x00"],
            ["café", "你好", "🙂"],
            ["x" * 200] * 100,
        ]
        for index, original in enumerate(cases):
            with self.subTest(case=index):
                encoded = Codec().encode(original.copy())
                self.assertIsInstance(encoded, str)
                decoded = Codec().decode(encoded)
                self.assertIsInstance(decoded, list)
                self.assertEqual(decoded, original)

    def test_independent_messages(self):
        encoder = Codec()
        first = encoder.encode(["a", "bc"])
        second = encoder.encode(["ab", "c"])
        self.assertIsInstance(first, str)
        self.assertIsInstance(second, str)
        self.assertNotEqual(first, second)
        decoder = Codec()
        self.assertEqual(decoder.decode(second), ["ab", "c"])
        self.assertEqual(decoder.decode(first), ["a", "bc"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
