from collections import Counter

class Solution:
    """
    This problem is asking to check if we can make two arrays equal by reversing subarrays of the first array.
    """

    def canBeEqual(self, target: list, arr: list) -> bool:
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        if len(target) != len(arr):
            return False
        if Counter(target) != Counter(arr):
            return False
        for i in range(len(arr)):
            left, right = 0, 0
            while left < i:
                right = i
                temp = arr[left:right]
                temp.reverse()
                arr[left:right] = temp
                if Counter(target) == Counter(arr):
                    return True
                right = i
                temp = arr[left:right]
                temp.reverse()
                arr[left:right] = temp
                if Counter(target) == Counter(arr):
                    return True
                left += 1
        return False