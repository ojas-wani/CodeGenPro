class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        target_count = n // 4
        for i, num in enumerate(arr):
            count = sum(1 for j in range(i, n) if arr[j] == num)
            if count > target_count:
                return num