class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        memo = {}
        def dfs(mask):
            if mask in memo:
                return memo[mask]
            res = 0
            for i, n in enumerate(nums):
                if mask & (1 << i):
                    res += dfs(mask ^ (1 << i)) ^ n
                else:
                    res += dfs(mask | (1 << i))
            memo[mask] = res
            return res
        return dfs(0)