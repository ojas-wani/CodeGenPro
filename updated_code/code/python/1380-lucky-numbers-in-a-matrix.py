from typing import List

class Solution:
    def __init__(self):  # Add an __init__ method to provide a docstring
        """
        This class is designed to solve the "Lucky Numbers in a Matrix" problem.
        It takes a 2D list of integers as input and returns a list of lucky numbers.
        A lucky number is an element that is the minimum in its row and maximum in its column.
        """
        pass

    def lucky_numbers(self, matrix: List[List[int]]) -> List[int]:
        """
        This method takes a 2D list of integers as input and returns a list of lucky numbers.
        A lucky number is an element that is the minimum in its row and maximum in its column.
        """
        m, n = len(matrix), len(matrix[0])
        result = []

        for i in range(m):
            min_val = min(matrix[i])
            for j in range(n):
                if matrix[i][j] == min_val and max(column(j, matrix)) == min_val:
                    result.append(min_val)
                    break

        return result

def column(j, matrix):
    return [row[j] for row in matrix]