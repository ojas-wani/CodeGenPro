class Solution:
    """
    Returns the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.

    Args:
        haystack (str): The string to search in.
        needle (str): The string to search for.

    Returns:
        int: The index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.
    """
    def str_str(self, haystack: str, needle: str) -> int:
        """
        Returns the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.

        Args:
            haystack (str): The string to search in.
            needle (str): The string to search for.

        Returns:
            int: The index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.
        """
        if needle == "":
            return 0
        if needle not in haystack:
            return -1
        try:
            return haystack.index(needle)
        except ValueError:
            return -1