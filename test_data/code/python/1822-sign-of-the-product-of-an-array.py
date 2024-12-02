class Solution:
    def arraySign(self, nums: List[int]) -> int:
        sign = 1
        zero_detected = False
        for num in nums:
            if num == 0:
                zero_detected = True
            elif num < 0:
                sign *= -1
        return sign if not zero_detected else 0