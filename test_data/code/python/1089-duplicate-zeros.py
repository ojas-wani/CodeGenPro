class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        n = len(arr) - 1
        while i < n:
            if arr[i] == 0:
                for j in range(n, i, -1):
                    arr[j] = arr[j-1]
                arr[i+1] = 0
                i += 1
                n -= 1
            else:
                i += 1