"""
Module to find the greatest common divisor of two strings.
"""
class GCDOfStrings:
    """
    Class to find the greatest common divisor of two strings.
    """

    def __gcd_of_strings__(self, str1: str, str2: str) -> str:
        """
        Returns the largest string `x` such that `x` divides both `str1` and `str2`.
        """
        if str1 + str2 != str2 + str1:
            return ""

        def gcd(a: int, b: int) -> int:
            """
            Calculate the greatest common divisor using the Euclidean algorithm.
            """
            while b:
                a, b = b, a % b
            return a

        length = gcd(len(str1), len(str2))
        return str1[:length]

# Example usage:
solution = GCDOfStrings()
print(solution.__gcd_of_strings__("ABCABC", "ABC"))  # Output: "ABC"
print(solution.__gcd_of_strings__("ABABAB", "ABAB"))  # Output: "AB"
print(solution.__gcd_of_strings__("LEET", "CODE"))  # Output: ""