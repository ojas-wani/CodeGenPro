class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if str(num).count(str(num)[0]) == len(str(num)):
                count += 1
        return count