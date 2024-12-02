Python
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        i = n - 1
        max_to_right = -1
        
        while i >= 0:
            temp = arr[i]
            arr[i] = max_to_right
            if i < n - 1:
                max_to_right = max(max_to_right, arr[i + 1])
            i -= 1
        
        return arr