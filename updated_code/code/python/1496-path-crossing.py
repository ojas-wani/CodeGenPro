class PathCrossingSolution:
    """
    This class defines a solution to the problem of determining if a path crosses itself.
    """

    def __init__(self):
        """
        Constructor for the PathCrossingSolution class.
        """

    def is_path_crossing(self, path: str) -> bool:
        """
        Determines if a path crosses itself.

        Args:
            path (str): A string of characters representing the path to traverse.

        Returns:
            bool: True if the path crosses itself, False otherwise.
        """
        x, y = 0, 0
        visited = set((0, 0))
        for direction in path:
            if direction == 'N':
                y += 1
            elif direction == 'S':
                y -= 1
            elif direction == 'E':
                x += 1
            elif direction == 'W':
                x -= 1
            if (x, y) in visited:
                return True
            visited.add((x, y))
        return False