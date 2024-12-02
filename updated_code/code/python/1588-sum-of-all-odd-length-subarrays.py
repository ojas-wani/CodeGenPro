import typing

class Solution:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        pass

    def sum_odd_length_subarrays(self, arr: typing.List[int]) -> int:
        """
        Calculate the sum of all possible odd-length subarrays.
        """
        n = len(arr)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + arr[i]

        total_sum = 0
        for length in range(1, n + 1, 2):
            for i in range(n - length + 1):
                total_sum += prefix_sum[i + length] - prefix_sum[i]

        return total_sum