class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        nums = [0, 1]
        for i in range(2, n + 1):
            if i * 2 <= n:
                nums.append(nums[i // 2])
            if i * 2 + 1 <= n:
                nums.append(nums[i // 2] + nums[(i + 1) // 2])
        return max(nums)