Python
class LongerNiceSubstring:
    """
    This class contains a method to find the longest nice substring from a given string.

    A string `s` is **nice** if, for every letter of the alphabet that `s` contains,
    it appears **both** in uppercase and lowercase.

    Args:
    self: The instance of the class.
    s (str): The input string.

    Returns:
    str: The longest **substring** of `s` that is **nice**.
    """
    def longest_nice_substring(self, s: str) -> str:
        if not s:
            return ""

        max_len = 0
        res = ""

        for i in range(len(s)):
            tmp_set = set()
            for j in range(i, len(s)):
                c = s[j]
                if c.lower() in tmp_set:
                    break
                if c not in tmp_set and c.lower() not in tmp_set:
                    tmp_set.add(c.lower())
                    tmp_set.add(c)
                if len(tmp_set) == 26:
                    if j - i + 1 > max_len:
                        max_len = j - i + 1
                        res = s[i:j+1]

        return res