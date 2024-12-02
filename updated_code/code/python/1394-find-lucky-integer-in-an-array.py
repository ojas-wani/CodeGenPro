from collections import Counter

class Solution:
    """
    This class is used to solve the problem of finding the largest lucky integer in an array.
    A lucky integer is an integer that has a frequency in the array equal to its value.
    """
    def find_lucky(self, arr: list) -> int:
        """
        This function finds the largest lucky integer in the input array.
        If there are no lucky integers, it returns -1.
        
        Parameters:
        arr (list): The input array of integers.
        
        Returns:
        int: The largest lucky integer in the array, or -1 if no lucky integer exists.
        """
        frequency = Counter(arr)
        lucky_numbers = [num for num, freq in frequency.items() if freq == num]
        return max(lucky_numbers) if lucky_numbers else -1