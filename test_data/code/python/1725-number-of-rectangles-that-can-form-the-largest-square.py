class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
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