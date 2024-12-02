"""
Module: Ball Factory
Description: This module calculates the maximum number of balls in a box.
"""

class BallFactory:
    """
    Class: BallFactory
    Description: This class is used to calculate the maximum number of balls in a box.
    """

    def __init__(self):
        """
        Method: __init__
        Description: Initializes the BallFactory object.
        """
        pass

    def count_balls(self, low_limit: int, high_limit: int) -> int:
        """
        Method: count_balls
        Description: This method calculates the maximum number of balls in a box.
        Parameters:
        low_limit (int): The lower limit of the balls.
        high_limit (int): The higher limit of the balls.
        Returns:
        int: The maximum number of balls in a box.
        """
        box_counts = {}
        for i in range(low_limit, high_limit + 1):
            digit_sum = sum(int(digit) for digit in str(i))
            box_counts[digit_sum] = box_counts.get(digit_sum, 0) + 1
        return max(box_counts.values())


if __name__ == "__main__":
    factory = BallFactory()
    print(factory.count_balls(1, 10))  # Output: 2