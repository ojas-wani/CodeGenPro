Python
import heapq
from typing import List

class Solution:
    """
    This class is used to find the k weakest rows in a matrix.
    The rows are considered weakest if they have fewer soldiers (1's) or if they have the same number of soldiers but have a lower index.

    :param mat: A 2D list of binary values where 1's represent soldiers and 0's represent civilians.
    :type mat: List[List[int]]
    :param k: The number of weakest rows to find.
    :type k: int
    :return: A list of indices of the k weakest rows in the matrix ordered from weakest to strongest.
    :rtype: List[int]
    """

    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        """
        This method finds the k weakest rows in a matrix.

        :param mat: A 2D list of binary values where 1's represent soldiers and 0's represent civilians.
        :type mat: List[List[int]]
        :param k: The number of weakest rows to find.
        :type k: int
        :return: A list of indices of the k weakest rows in the matrix ordered from weakest to strongest.
        :rtype: List[int]
        """

        # Count the number of soldiers in each row and store them in a list along with their indices.
        soldier_count = [(row.count(1), i) for i, row in enumerate(mat)]

        # Turn the list into a heap so that it is ordered from smallest to largest.
        heapq.heapify(soldier_count)

        # Initialize an empty list to store the indices of the k weakest rows.
        weakest_rows = []

        # Loop through the heap until it is empty or we've found k weakest rows.
        while soldier_count and k > 0:
            # Pop the smallest element from the heap and add its index to our list.
            k -= 1
            weakest_rows.append(heapq.heappop(soldier_count)[1])

        # Return the list of indices of the k weakest rows.
        return weakest_rows