Python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = 0
        sorted_nums = sorted((x - 1 for x in nums), reverse=True)
        for i, num in enumerate(sorted_nums):
            if i == len(sorted_nums) - 1:
                break
            max_product = max(max_product, (num + 1) * sorted_nums[i + 1])
        return max_product