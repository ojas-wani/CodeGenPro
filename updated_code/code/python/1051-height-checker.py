class HeightChecker:
    def __init__(self):
        """
        Initializes the HeightChecker class.
        """
        pass

    def heightChecker(self, heights: list) -> int:
        """
        This function takes a list of integer heights as input, sorts them, and then checks
        the count of indices where the heights in the original list are different from
        the heights in the sorted list.

        Args:
            heights (list): A list of integer heights.

        Returns:
            int: The number of indices where the heights in the original list are different
                 from the heights in the sorted list.
        """
        expected = sorted(heights)
        return sum(a != b for a, b in zip(heights, expected))