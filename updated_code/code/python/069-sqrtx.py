Python
def sqrt_x(x: int) -> int:
    """
    Given a non-negative integer `x`, return the square root of `x` rounded down to the nearest integer.

    Args:
    x (int): A non-negative integer.

    Returns:
    int: The square root of `x` rounded down to the nearest integer.
    """
    if x == 0:
        return 0

    start, end = 1, x
    while start <= end:
        mid = start + (end - start) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            start = mid + 1
        else:
            end = mid - 1

    return start - 1