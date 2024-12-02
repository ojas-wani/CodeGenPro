class ClimbingStairs:
    """
    This class will solve the issue related to climbing stairs.
    """
    
    def __init__(self):
        """
        Initialize the class.
        """
        pass

    def climb_stairs(self, n: int) -> int:
        """
        This method calculates the number of distinct ways to climb the stairs.

        Args:
        n (int): The number of steps in the stairs.

        Returns:
        int: The number of distinct ways to climb the stairs.
        """
        if n <= 2:
            return n
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b


if __name__ == '__main__':
    obj = ClimbingStairs()
    print(obj.climb_stairs(2))   # Output: 2
    print(obj.climb_stairs(3))   # Output: 3