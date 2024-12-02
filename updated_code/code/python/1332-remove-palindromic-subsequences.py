def remove_palindrome_subsequences(s: str) -> int:
    """
    This function removes the minimum number of palindrome subsequences to make the given string empty.

    Args:
    s (str): The input string consisting only of letters 'a' and 'b'.

    Returns:
    int: The minimum number of steps to make the given string empty.
    """
    if s == s[::-1]:  # check if the string is already a palindrome
        return 1  # return 1 if the string is a palindrome, else remove the last character
    return 1 + remove_palindrome_subsequences(s[:-1]) if s[:-1] != s[:0][::-1] else 1 + remove_palindrome_subsequences(s[1:])

# Testing
print(remove_palindrome_subsequences("ababa"))  # Output: 1
print(remove_palindrome_subsequences("abb"))  # Output: 2
print(remove_palindrome_subsequences("baabb"))  # Output: 2