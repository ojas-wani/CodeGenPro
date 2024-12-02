class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        box_counts = {}
        for i in range(lowLimit, highLimit + 1):
            digit_sum = sum(int(digit) for digit in str(i))
            box_counts[digit_sum] = box_counts.get(digit_sum, 0) + 1
        return max(box_counts.values())