class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_start_value = 1
        total = 0
        for num in nums:
            total += num
            if total < 1:
                min_start_value = max(min_start_value, 1 - total)
        return min_start_value