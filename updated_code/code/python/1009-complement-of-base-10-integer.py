"""
This script calculates the bitwise complement of a given number.

The **complement** of an integer is the integer you get when you flip all the
`0`'s to `1`'s and all the `1`'s to `0`'s in its binary representation.

For example, the integer `5` is `"101"` in binary and its **complement** is `"010"` which is the integer `2`.

Given an integer `n`, return _its complement_.
"""

class Solution:
    """
    This class calculates the bitwise complement of a given number.
    """
    
    def bitwise_complement(self, n: int) -> int:
        """
        Calculate the bitwise complement of a given number.

        Args:
            n (int): The input number.

        Returns:
            int: The bitwise complement of the input number.
        """
        if n == 0:
            return 1
        # Convert the integer to binary, remove the '0b' prefix, and flip all the bits
        complement = int(bin(n^((1<<n.bit_length())-1))[2:], 2)
        return complement