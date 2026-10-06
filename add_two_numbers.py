"""LeetCode 2: Add Two Numbers — local practice (Python 3.10+).

Two nonempty linked lists represent nonnegative integers. Each node holds
one digit, with the least significant digit first. Return their sum as a
linked list in the same reverse order. Inputs have no leading zeros except
for the number zero itself.

Example: [2, 4, 3] + [5, 6, 4] -> [7, 0, 8], because 342 + 465 = 807.
The bracket notation describes linked-list digits, not Python-list inputs.

Implement ONLY Solution.addTwoNumbers, then run:
    python add_two_numbers.py

No packages to install. The starter intentionally raises NotImplementedError;
all 10 tests will report errors until you implement your solution.
"""

from __future__ import annotations
import unittest


class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        # Write your solution here. Return the head of the result linked list.
        
        #l1 = list 1
        #l2 = list 2
        # return l3
        """
        1. Initialize Pointers and Carry
        2. Traverse and Compute Sums
        3. Update Carry and Append Nodes
        4. Return the Result Head
        """
        dummy = ListNode()
        current = dummy
        carry = 0
        
        while l1 is not None or l2 is not None or carry:
            digit1 =l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0
            
            total = digit1 + digit2 + carry
            carry = total // 10
            digit = total % 10
            
            current.next = ListNode(digit)
            current = current.next

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        return dummy.next
        
        
        # END OF SOLUTION
        raise NotImplementedError("Implement addTwoNumbers to begin practicing.")


# Test helpers: these build and inspect linked lists for the tests.
# You do not need to edit them or use them in your solution.
def build_linked_list(digits: list[int]) -> ListNode | None:
    head = None
    for digit in reversed(digits):
        head = ListNode(digit, head)
    return head


def linked_list_to_list(head: ListNode | None) -> list[int]:
    digits = []
    visited = set()
    while head is not None:
        if not isinstance(head, ListNode):
            raise AssertionError("Return a ListNode chain, not a Python list or integer.")
        if id(head) in visited:
            raise AssertionError("Your result contains a cycle in its next pointers.")
        visited.add(id(head))
        if type(head.val) is not int or not 0 <= head.val <= 9:
            raise AssertionError("Each node must contain one integer digit from 0 to 9.")
        digits.append(head.val)
        head = head.next
    return digits


class TestAddTwoNumbers(unittest.TestCase):
    def check_sum(self, first, second, expected):
        result = Solution().addTwoNumbers(
            build_linked_list(first), build_linked_list(second)
        )
        self.assertEqual(linked_list_to_list(result), expected)

    def test_example(self):
        self.check_sum([2, 4, 3], [5, 6, 4], [7, 0, 8])

    def test_both_zero(self):
        self.check_sum([0], [0], [0])

    def test_repeated_carry(self):
        self.check_sum([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9],
                       [8, 9, 9, 9, 0, 0, 0, 1])

    def test_single_digits_no_carry(self):
        self.check_sum([2], [5], [7])

    def test_extra_final_node(self):
        self.check_sum([5], [5], [0, 1])

    def test_first_list_longer(self):
        self.check_sum([1, 2, 3], [4], [5, 2, 3])

    def test_second_list_longer(self):
        self.check_sum([4], [1, 2, 3], [5, 2, 3])

    def test_zero_plus_number(self):
        self.check_sum([0], [0, 1, 2], [0, 1, 2])

    def test_carry_stops_in_middle(self):
        self.check_sum([9, 1, 2], [1], [0, 2, 2])

    def test_long_carry_chain(self):
        self.check_sum([9] * 100, [1], [0] * 100 + [1])


if __name__ == "__main__":
    unittest.main(verbosity=2)
