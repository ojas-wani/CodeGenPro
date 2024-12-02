class GenerateArraySolution:
    """
    This class contains a method to generate an array according to the given rules and return the maximum value in the array.

    The method getMaximumGenerated generates an arraynums of size n + 1 based on the given rules.
    The rules are:
        * nums[0] = 0
        * nums[1] = 1
        * nums[2 * i] = nums[i] when 2 <= 2 * i <= n
        * nums[2 * i + 1] = nums[i] + nums[i + 1] when 2 <= 2 * i + 1 <= n

    The maximum value in the array is returned as the result.
    """

    def get_maximum_generated(self, n: int) -> int:
        """
        Returns the maximum value in the array generated according to the given rules.
        
        :param n: The size of the array to be generated.
        :return: The maximum value in the array.
        """
        if n == 0:
            return 0
        nums = [0, 1]
        for i in range(2, n + 1):
            if i * 2 <= n:
                nums.append(nums[i // 2])
            if i * 2 + 1 <= n:
                nums.append(nums[i // 2] + nums[(i + 1) // 2])
        return max(nums)


# Example usage:
solution = GenerateArraySolution()
print(solution.get_maximum_generated(7))  # Output: 3