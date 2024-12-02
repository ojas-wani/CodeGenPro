class Solution:
    """
    This class defines a method `areAlmostEqual` that returns True if two strings can be made equal by performing at most one string swap on exactly one of the strings, and False otherwise.
    """

    def areAlmostEqual(self, a: str, b: str) -> bool:
        """
        This method checks if two strings can be made equal by performing at most one string swap on exactly one of the strings.
        
        Parameters:
        a (str): The first string.
        b (str): The second string.
        
        Returns:
        bool: True if the strings can be made equal by performing at most one string swap on exactly one of the strings, and False otherwise.
        """
        
        # If the strings are equal, they can be made equal by performing no swaps
        if a == b:
            return True

        # Initialize variables to track the number of differences and the indices of the differences
        diff_count = 0
        diff_indices = []

        # Iterate over the characters in the strings
        for i in range(len(a)):
            # If the characters at the current index are different
            if a[i] != b[i]:
                # Increment the difference count
                diff_count += 1
                # Add the current index to the list of indices
                diff_indices.append(i)
                # If more than two differences are found, it is not possible to make the strings equal by performing at most one string swap
                if diff_count > 2:
                    return False

        # If exactly two differences are found, it is possible to make the strings equal by performing at most one string swap
        if diff_count == 2:
            # Swap the characters at the two different indices
            a = list(a)
            a[diff_indices[0]], a[diff_indices[1]] = a[diff_indices[1]], a[diff_indices[0]]
            # If the strings are now equal, return True
            if ''.join(a) == b:
                return True

        # If the strings cannot be made equal by performing at most one string swap, return False
        return False