class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        total_sum = sum(nums)
        result = []
        subsequence_sum = 0
        for num in nums:
            if subsequence_sum + num > total_sum - subsequence_sum:
                result.append(num)
                subsequence_sum += num
            else:
                break
        return result