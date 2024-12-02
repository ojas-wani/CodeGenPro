class XorOperation:
    """
    Class to perform bitwise XOR operation on an array.
    """

    """
    Method to perform bitwise XOR operation on an array.
    Args:
        n (int): The size of the array.
        start (int): The starting value of the array.
    Returns:
        int: The bitwise XOR of all elements in the array.
    """
    def xor_operation(self, n: int, start: int) -> int:
        result = 0
        for i in range(n):
            result ^= start + 2 * i
        return result