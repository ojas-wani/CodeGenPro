class ValidParentheses:
    """
    This class determines if the input string is valid.
    """
    def __init__(self):
        """
        Constructor for the ValidParentheses class.
        """
        pass

    def is_valid(self, s: str) -> bool:
        """
        Determine if the input string is valid.
        
        Parameters:
        s (str): The input string containing parentheses.
        
        Returns:
        bool: True if the string is valid, False otherwise.
        """
        if len(s) % 2 != 0:
            return False
        
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping:
                if not stack or mapping[char] != stack.pop():
                    return False
        
        return not stack