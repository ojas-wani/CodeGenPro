class solution:
    """
    This class solves the problem of counting the number of '1' bits in the binary representation of an unsigned integer.
    """

    def hamming_weight(self, n: int) -> int:
        """
        This function takes the binary representation of an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

        Args:
            n (int): The input integer.

        Returns:
            int: The number of '1' bits in the binary representation of the input integer.
        """
        return bin(n).count('1')