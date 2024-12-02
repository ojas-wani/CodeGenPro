class SumOfUniqueElements:
    """
    This class calculates the sum of unique elements in a given list of integers.

    :param nums: A list of integers.
    :return: The sum of unique elements.
    """

    def sum_of_unique(self, nums: list[int]) -> int:
        """
        This function calculates the sum of unique elements in a given list of integers.

        :param nums: A list of integers.
        :return: The sum of unique elements.
        """

        # Check if the input is a list
        if not isinstance(nums, list):
            raise TypeError("Input must be a list of integers.")

        # Count the occurrences of each integer in the list
        num_count = {}
        for num in nums:
            if num in num_count:
                num_count[num] += 1
            else:
                num_count[num] = 1

        # Calculate the sum of unique elements
        sum_unique = sum(num for num, count in num_count.items() if count == 1)

        return sum_unique