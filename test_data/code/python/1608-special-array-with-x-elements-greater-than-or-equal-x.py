class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums), 0, -1):
            if i <= len(nums) and nums[i-1] >= i:
                return i
        return -1