def trim_mean(arr):
    """
    Given an integer array `arr`, return _the mean of the remaining integers after
    removing the smallest`5%` and the largest `5%` of the elements_.

    Args:
        arr (List[int]): The input array

    Returns:
        float: The mean of the remaining integers
    """
    import math

    arr.sort()
    n = len(arr)
    total = sum(arr)
    percent = int(n * 0.05)

    # Remove the smallest 5% and the largest 5% of the elements
    arr = arr[percent:n - percent]
    mean = total / len(arr)

    return mean