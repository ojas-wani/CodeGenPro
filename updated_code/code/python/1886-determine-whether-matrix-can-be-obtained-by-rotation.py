from typing import List

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        """
        Determine whether a given matrix can be obtained by rotating another matrix in 90-degree increments.

        Args:
        mat (List[List[int]]): The given matrix.
        target (List[List[int]]): The target matrix.

        Returns:
        bool: True if the matrix can be obtained by rotating the target matrix, False otherwise.
        """
        def rotate(mat):
            """
            Rotate the given matrix 90 degrees clockwise.

            Args:
            mat (List[List[int]]): The given matrix.

            Returns:
            List[List[int]]: The rotated matrix.
            """
            return [list(x) for x in zip(*mat)][::-1]

        for _ in range(4):
            if mat == target:
                return True
            mat = rotate(mat)
        return False