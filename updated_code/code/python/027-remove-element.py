class Solution:
    """
    This is the solution class for the remove elements problem.
    """
    def removeElement(self, nums: list, val: int) -> int:
        """
        This function removes all occurrences of val from the input list nums.
        The first k elements of the list contain the elements which are not equal to val.
        The remaining elements of the list are not important as well as the size of the list.
        The function returns k.
        """
        k = 0
        for num in nums:
            if num != val:
                nums[k] = num
                k += 1
        return k