Python
class ReverseBits:
    """
    This class contains a method that reverses the bits of a given 32-bit unsigned integer.

    Args:
    n (int): A 32-bit unsigned integer.

    Returns:
    int: The reversed 32-bit unsigned integer.
    """
    def reverseBits(self, n: int) -> int:
        """
        This method reverses the bits of a given 32-bit unsigned integer.

        Args:
        n (int): A 32-bit unsigned integer.

        Returns:
        int: The reversed 32-bit unsigned integer.
        """
        result = 0
        for _ in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1
        return result


# Add a newline at the end of the file