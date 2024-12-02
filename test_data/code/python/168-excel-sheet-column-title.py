class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while columnNumber > 0:
            columnNumber, remainder = divmod(columnNumber - 1, 26)
            result = chr(65 + remainder) + result
        return result