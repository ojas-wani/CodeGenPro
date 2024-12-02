Python
class NumberOfStringSteps:
    """
    Class to solve the problem of number of steps to reduce a number to zero.
    """

    def __int__(self):
        """
        Constructor for the class
        """

    def number_of_steps(self, num: int) -> int:
        """
        This function calculates the number of steps to reduce the given number to zero.
        In one step, if the current number is even, you have to divide it by `2`,
        otherwise, you have to subtract `1` from it.
        
        Args:
            num (int): The input number
            
        Returns:
            int: The number of steps to reduce the input number to zero
        """
        steps = 0
        while num > 0:
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
            steps += 1
        return steps

# Testing the code
solution = NumberOfStringSteps()
print(solution.number_of_steps(14))  # Output: 6
print(solution.number_of_steps(8))   # Output: 4
print(solution.number_of_steps(123))  # Output: 12