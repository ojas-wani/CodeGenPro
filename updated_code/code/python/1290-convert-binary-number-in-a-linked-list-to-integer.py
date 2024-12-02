from __future__ import print_function
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    This class contains the getDecimalValue method that converts a binary number
    represented as a linked list to its decimal equivalent.

    Args:
    head: A reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1.

    Returns:
    The decimal value of the number in the linked list.

    The most significant bit is at the head of the linked list.
    """
    def get_decimal_value(self, head: Optional[ListNode]) -> int:
        """
        This method converts a binary number represented as a linked list to its decimal equivalent.

        Args:
        head: A reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1.

        Returns:
        The decimal value of the number in the linked list.

        The most significant bit is at the head of the linked list.
        """
        result = 0
        while head:
            # Shift the result to the left by one bit and add the value of the current node
            result = (result << 1) | head.val
            head = head.next
        return result

if __name__ == "__main__":
    pass