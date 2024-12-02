Python
from typing import List

class SortIntegersByTheNumber:
    """
    This class is used to sort integers in an array in ascending order by the number of 1's in their binary representation.
    If two or more integers have the same number of 1's, they are sorted in ascending order.
    """

    def sort_by_bits(self, arr: List[int]) -> List[int]:
        """
        This method sorts the integers in the array in ascending order by the number of 1's in their binary representation.
        If two or more integers have the same number of 1's, they are sorted in ascending order.

        Parameters:
        arr (List[int]): The input array of integers.

        Returns:
        List[int]: The array after sorting it.
        """
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))