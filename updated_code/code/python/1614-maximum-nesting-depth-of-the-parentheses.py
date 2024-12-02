class MaximumNestingDepthOfParentheses:
    """
    This class is used to calculate the maximum nesting depth of a valid 
    parentheses string.
    """

    def max_depth(self, s: str) -> int:
        """
        This function calculates the maximum nesting depth of a valid 
        parentheses string.

        Args:
            s (str): The valid parentheses string.

        Returns:
            int: The maximum nesting depth of the valid parentheses string.
        """

        max_depth = 0
        current_depth = 0

        for char in s:
            if char == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                current_depth -= 1

        return max_depth