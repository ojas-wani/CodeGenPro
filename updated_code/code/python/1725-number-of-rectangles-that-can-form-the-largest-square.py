from typing import List

class Solution:
    """
    This is a solution to the problem of counting the number of rectangles that can form the largest square.
    """
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        """
        This method takes a list of rectangles as input, where each rectangle is represented as a list of two integers, 
        representing the length and width of the rectangle. It returns the number of rectangles that can form a square 
        with a side length equal to the largest square that can be formed by any of the given rectangles.
        """
        max_len = 0
        count = 0
        for length, width in rectangles:
            min_len = min(length, width)
            if min_len > max_len:
                max_len = min_len
                count = 1
            elif min_len == max_len:
                count += 1
        return count