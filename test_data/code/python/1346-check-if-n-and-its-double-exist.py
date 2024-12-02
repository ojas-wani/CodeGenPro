Python
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i != j and (arr[i] == 2 * arr[j] or arr[i] % 2 == 0 and arr[i] // 2 in arr):
                    return True
        return False