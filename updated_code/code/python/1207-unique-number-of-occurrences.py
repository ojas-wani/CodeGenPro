# Define the import statement at the top of the file
from collections import Counter

class Solution:
    """
    This class contains a method called uniqueOccurrences which takes an array of integers as input
    and returns True if the number of occurrences of each value in the array is unique or False otherwise.
    """

    """
    This method takes an array of integers as input
    and returns True if the number of occurrences of each value in the array is unique or False otherwise.
    """
    def uniqueOccurrences(self, arr: list) -> bool:
        count_dict = Counter(arr)
        return len(set(count_dict.values())) == len(count_dict)