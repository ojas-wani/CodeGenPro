Python
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0
        for num in arr1:
            flag = True
            for num2 in arr2:
                if abs(num - num2) <= d:
                    flag = False
                    break
            if not flag:
                continue
            count += 1
        return count