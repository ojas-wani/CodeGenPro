class Solution:
    """
    The Solution class contains a method removeDuplicates to solve the problem.
    This method removes the duplicates from the sorted array and returns the number of unique elements.
    """

    def removeDuplicates(self, nums: list[int]) -> int:
        """
        This function removes the duplicates from the sorted array and returns the number of unique elements.
        :param nums: The input array containing integers.
        :return: The number of unique elements in the input array.
        """
        if len(nums) == 0:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1
