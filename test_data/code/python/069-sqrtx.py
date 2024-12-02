class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        start, end = 1, x
        while start <= end:
            mid = start + (end - start) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                start = mid + 1
            else:
                end = mid - 1
        
        return end