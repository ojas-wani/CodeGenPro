class Solution:
    """
    Description:
    You are given a **0-indexed** string `s` that has lowercase English letters in
    its **even** indices and digits in its **odd** indices.

    There is a function `shift(c, x)`, where `c` is a character and `x` is a
    digit, that returns the `xth` character after `c`.

    For every **odd**  index `i`, you want to replace the digit `s[i]` with
    `shift(s[i-1], s[i])`.

    Return `s` _after replacing all digits. It is **guaranteed** that
    `_shift(s[i-1], s[i])` _will never exceed_ `'z'`.
    """

    def replaceDigits(self, s: str) -> str:
        """
        Replaces all digits in the given string with characters.
        """
        result = list(s)  # Convert the input string to a list
        for i in range(1, len(s), 2):  # Iterate over the odd indices
            prev = result[i - 1]  # The previous character
            curr = result[i]  # The current digit
            result[i] = chr(ord(prev) + int(curr))  # Replace the digit with the shifted character
        return ''.join(result)  # Convert the list back to a string

# Add a newline at the end of the file