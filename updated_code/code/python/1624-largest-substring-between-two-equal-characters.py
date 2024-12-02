class Solution:
    """
    Given a string `s`, return the length of the longest substring between two equal characters, excluding the two characters.
    If there is no such substring, return `-1`.
    """
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        """
        Initialize an empty dictionary `char_index` to store the last index of each character.
        Initialize `max_len` to `-1` to store the maximum length of the substring.
        
        Iterate over the string `s` using the `enumerate` function to get both the index `i` and the character `char`.
        
        If the character is in `char_index`, calculate the length of the substring between the last occurrence of the character and the current occurrence, and update `max_len` if necessary.
        If the character is not in `char_index`, add it to `char_index` with its current index.
        
        Return `max_len` as the result.
        """
        char_index = {}
        max_len = -1
        
        for i, char in enumerate(s):
            if char in char_index:
                max_len = max(max_len, i - char_index[char] - 1)
            else:
                char_index[char] = i
        
        return max_len