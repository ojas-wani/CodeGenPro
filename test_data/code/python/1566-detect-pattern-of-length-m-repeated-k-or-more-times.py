Python
class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        for i in range(len(arr) - m * k + 1):
            pattern = arr[i:i+m]
            for j in range(k-1):
                if arr[i+j*m:i+(j+1)*m] != pattern:
                    break
            else:
                return True
        return False