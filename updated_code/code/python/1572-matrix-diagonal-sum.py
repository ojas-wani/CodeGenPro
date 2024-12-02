Python
class MatrixDiagonalSum:
    """
    This class implements the diagonal sum of a square matrix.
    """
    def __init__(self):
        """
        Initializes the class.
        """
        pass

    def diagonalSum(self, mat: list[list[int]]) -> int:
        """
        This function calculates the sum of the matrix diagonals.
        It adds the sum of the primary diagonal and the sum of the secondary diagonal that are not part of the primary diagonal.
        If the matrix size is odd, it subtracts the middle element since it is counted twice.
        :param mat: A square matrix.
        :return: The sum of the matrix diagonals.
        """
        n = len(mat)
        total_sum = 0
        for i in range(n):
            total_sum += mat[i][i]
            total_sum += mat[i][n - i - 1]
        if n % 2 != 0:
            total_sum -= mat[n // 2][n // 2]
        return total_sum