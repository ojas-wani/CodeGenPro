from typing import List

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
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