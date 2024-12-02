class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev_one = -1
        for i, num in enumerate(nums):
            if num == 1:
                if prev_one != -1 and i - prev_one <= k:
                    return False
                prev_one = i
        return True