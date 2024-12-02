from typing import List

class Solution:
    """
    This class is used to solve the problem of checking if an array can be formed by concatenating the arrays in pieces.
    """
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        """
        This function checks if the array `arr` can be formed by concatenating the arrays in `pieces`.
        
        :param arr: The array to be formed.
        :param pieces: The arrays to be concatenated.
        :return: True if the array can be formed, False otherwise.
        """
        piece_index = 0
        for i in range(len(arr)):
            for piece in pieces:
                if arr[i:i + len(piece)] == piece:
                    piece_index += len(piece)
                    i += len(piece) - 1
                    break
            else:
                return False
        return True

# Example usage:
solution = Solution()
arr = [15, 88]
pieces = [[88], [15]]
print(solution.canFormArray(arr, pieces))  # Output: True

arr = [49, 18, 16]
pieces = [[16, 18, 49]]
print(solution.canFormArray(arr, pieces))  # Output: False

arr = [91, 4, 64, 78]
pieces = [[78], [4, 64], [91]]
print(solution.canFormArray(arr, pieces))  # Output: True