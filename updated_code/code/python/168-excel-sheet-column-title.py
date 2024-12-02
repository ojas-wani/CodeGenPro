Python
class ExcelSheetColumnTitle:
    """
    This class is designed to convert an integer to its corresponding column title as it appears in an Excel sheet.
    """

    def convert_to_title(self, column_number: int) -> str:
        """
        This function converts an integer to its corresponding column title as it appears in an Excel sheet.

        Parameters:
        column_number (int): The integer to be converted to column title.

        Returns:
        str: The column title corresponding to the given integer.

        """
        result = ""
        while column_number > 0:
            column_number, remainder = divmod(column_number - 1, 26)
            result = chr(65 + remainder) + result
        return result


# Example usage:
excel_sheet = ExcelSheetColumnTitle()
print(excel_sheet.convert_to_title(1))  # Output: "A"
print(excel_sheet.convert_to_title(28))  # Output: "AB"
print(excel_sheet.convert_to_title(701))  # Output: "ZY"