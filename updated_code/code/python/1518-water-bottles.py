class WaterBottles:
    """
    A Python class to simulate water bottles and calculate the maximum amount of water bottles that can be drunk
    """

    def __init__(self):
        """
        Initialize the class
        """

    def num_water_bottles(self, num_bottles: int, num_exchange: int) -> int:
        """
        Calculate the maximum number of water bottles that can be drunk

        Args:
        num_bottles (int): The initial number of full bottles
        num_exchange (int): The number of empty bottles that can be exchanged for one full bottle

        Returns:
        int: The maximum number of water bottles that can be drunk
        """
        empty_bottles = num_bottles
        full_bottles = num_bottles
        total_bottles = full_bottles
        while empty_bottles >= num_exchange:
            new_full_bottles = empty_bottles // num_exchange
            empty_bottles = (empty_bottles % num_exchange) + new_full_bottles
            full_bottles += new_full_bottles
            total_bottles += new_full_bottles
        return total_bottles


if __name__ == "__main__":
    solution = WaterBottles()
    print(solution.num_water_bottles(9, 3))  # Output: 13
    print(solution.num_water_bottles(15, 4))  # Output: 19