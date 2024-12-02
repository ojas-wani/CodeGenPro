import collections.abc

class Solution:
    """
    Decompresses a list of integers representing a list compressed with run-length encoding.

    For each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0),
    there are `freq` elements with value `val` concatenated in a sublist.
    Concatenate all the sublists from left to right to generate the decompressed list.
    """

    def decompressRLElist(self, nums: list) -> list:
        """
        Decompresses a list compressed with run-length encoding.

        Args:
            nums (list): A list of integers representing a list compressed with run-length encoding.

        Returns:
            list: The decompressed list.
        """
        decompressed_list = []
        frequency_value = collections.abc iterate(nums, 2)
        for frequency, value in frequency_value:
            decompressed_list.extend([value] * frequency)
        return decompressed_list