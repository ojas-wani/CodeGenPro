def chessboard_color(coordinates: str) -> bool:
    """
    Check if the chessboard square is white or black.

    Args:
        coordinates (str): The coordinates of the chessboard square.

    Returns:
        bool: True if the square is white, False if it's black.
    """
    # Check if the given coordinate is valid
    if not (ord('a') <= ord(coordinates[0]) <= ord('h') and
            ord('1') <= ord(coordinates[1]) <= ord('8')):
        raise ValueError("Invalid coordinates")

    # The square is white if the sum of the position is odd
    # The position of a square in a chessboard can be represented as a 2-tuple
    # where the first element is the rank and the second element is the file.
    # The rank is the row, and the file is the column.
    # The rank is numbered from 1 to 8, and the file is lettered from a to h.
    # So, the position of the square with the ranks and files as R and f is
    # (R, f). The position of the square with the ranks and files as E and e is
    # (E, e).
    row = int(coordinates[1])
    col = ord(coordinates[0]) - ord('a') + 1
    return (row + col) % 2 == 1