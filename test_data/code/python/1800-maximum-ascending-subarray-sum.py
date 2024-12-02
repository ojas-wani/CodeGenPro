class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum, dp = 0, [0]
        
        for num in nums:
            if dp[-1] + num > num:
                dp[-1] += num
            else:
                dp.append(num)
            max_sum = max(max_sum, max(dp))
        
        return max_sum