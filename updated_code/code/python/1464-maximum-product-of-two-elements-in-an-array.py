class Solution:
    """
    Given the array of integers `nums`, you will choose two different indices `i`
    and `j` of that array. _Return the maximum value of_
    `(nums[i]-1)*(nums[j]-1)`.

    Args:
        nums (List[int]): The input list of integers.

    Returns:
        int: The maximum value of `(nums[i]-1)*(nums[j]-1)`.
    """
    def max_product(self, nums: List[int]) -> int:
        """Return the maximum value of `(nums[i]-1)*(nums[j]-1)`."""
        nums.sort()  # Sort the array in ascending order
        return (nums[-1] - 1) * (nums[-2] - 1)  # Return the maximum product