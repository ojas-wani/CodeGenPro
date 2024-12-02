class Solution:
    def thousandSeparator(self, n: int) -> str:
        n_str = str(n)
        result = ""
        for i, char in enumerate(n_str[::-1]):
            if i % 3 == 0 and i != 0:
                result = "." + result
            result = char + result
        return "0" + result if n != 0 else "0"