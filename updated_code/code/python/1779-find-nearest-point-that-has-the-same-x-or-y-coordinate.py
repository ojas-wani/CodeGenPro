class nearest_valid_point_solution:
    """
    This class solves the problem of finding the nearest valid point
    that has the same x or y coordinate as the given point.
    """

    def __init__(self):
        """
        Constructor for the class.
        """

    def nearest_valid_point(self, x: int, y: int, points: List[List[int]]) -> int:
        """
        This function returns the index of the valid point with the smallest Manhattan distance
        from the current location. If there are multiple valid points, it returns the one
        with the smallest index. If there are no valid points, it returns -1.

        Args:
            x (int): The x-coordinate of the current location.
            y (int): The y-coordinate of the current location.
            points (List[List[int]]): A list of points, where each point is a list of two integers.

        Returns:
            int: The index of the valid point with the smallest Manhattan distance.
        """
        min_dist = float('inf')
        min_idx = -1
        for i, (px, py) in enumerate(points):
            if px == x or py == y:
                dist = abs(px - x) + abs(py - y)
                if dist < min_dist:
                    min_dist = dist
                    min_idx = i
        return min_idx