import os
from openpyxl import load_workbook
import pandas as pd


def update_existing_column_excel(file_path, column_name, column_data):
    """
    Updates an existing empty column in an Excel file with new data.

    Args:
        file_path (str): Path to the Excel file.
        column_name (str): Name of the column to be updated.
        column_data (list): Data for the column, must match the number of rows in the sheet.
    """
    # Load the workbook and identify the active sheet
    workbook = load_workbook(file_path)
    sheet = workbook.active

    # Read the existing data into a DataFrame
    existing_data = pd.DataFrame(sheet.values)
    # Set first row as column headers
    existing_data.columns = existing_data.iloc[0]
    existing_data = existing_data[1:]  # Remove the header row from the data

    # Ensure the column exists in the file
    if column_name not in existing_data.columns:
        raise ValueError(
            f"The column '{column_name}' does not exist in the Excel file.")

    # Update the empty column with new data
    if len(column_data) != len(existing_data):
        raise ValueError(
            "Length of column_data must match the number of rows in the existing data.")
    existing_data[column_name] = column_data

    # Save the updated DataFrame back to the Excel file
    with pd.ExcelWriter(file_path, engine="openpyxl", mode="w") as writer:
        existing_data.to_excel(writer, index=False, startrow=1)

    print(f"Column '{column_name}' updated successfully.")

# Count how many lines of codes have flake8 issues


def filter_python_flake8(flake8_report_txt_path, file_name) -> int:
    """Filter Python code for specific issues detected by flake8."""
    report_path = flake8_report_txt_path
    code_style_count = 0

    flake8_codes = [
        "E111",  # Indentation is not a multiple of four
        "E112",  # Expected an indented block
        "E113",  # Unexpected indentation
        "E114",  # Indentation is not a multiple of four (comment)
        "E115",  # Expected an indented block (comment)
        "E116",  # Unexpected indentation (comment)
        "E501",  # Line too long
        "B006",  # Mutable defaults
        "B950"   # Line too long (adjusted threshold)
    ]

    flake8_codes = ['E1135']

    with open(report_path, "r") as f:
        lines = f.readlines()

    # if not lines:

    for line in lines:
        line = line.replace(
            f"ChatGPT-CodeGenAnalysis-main/test_data/temp/code/", "")

        if line.split(" ")[1] in flake8_codes:
            code_style_count = 1
            break

    return code_style_count


def filter_python_pylint(pylint_report_txt_path, file_name):
    """Filter Python code for specific issues detected by pylint."""
    report_path = pylint_report_txt_path
    code_style_count = 0

    pylint_codes = [
        "C0330",  # Wrong continued indentation
        "W0311",  # Bad indentation (not a multiple of four)
        "C0301",  # Line too long
        "C0209"   # Suggests better variable names
    ]

    with open(report_path, "r") as f:
        lines = f.readlines()

    lines.pop(0)

    for line in lines:
        print(line.split(": "))

        if len(line.split(": ")) < 2:
            continue

        if line.split(": ")[1] in pylint_codes:
            code_style_count = 1
            break

    return code_style_count


def filter_java_checkstyle(checkstyle_report_txt_path, file_name):
    """Filter Java code for specific issues detected by Checkstyle."""
    report_path = checkstyle_report_txt_path
    code_style_count = 0

    remove_list = [
        "Indentation",      # Consistent indentation
        "LineLength",       # Overly long lines
        "LocalVariableName",  # Meaningful local variable names
        "MemberName",       # Proper member variable naming
        "ConstantName",     # Proper constant naming
        "MethodName",       # Descriptive method names
        "TypeName",         # Proper class / interface names
        "WhitespaceAround",  # Consistent whitespace
        "NeedBraces"  # Proper braces for block structures
    ]

    with open(report_path, "r") as f:
        lines = f.readlines()

    for line in lines:
        if line.startswith("[ERROR]"):
            line = line.replace("[ERROR] ", "")
            line = line.replace(
                rf"LLM-Improved-Code-Quality\test_data\temp\code\java\{file_name}", "")
            type_smell = line.split(". [")[1].replace("]", "").strip()

            if type_smell in remove_list:
                code_style_count = 1
                break

    return [str(code_style_count)]


def filter_java_pmd(pmd_report_txt_path, file_name):
    """Filter Java code for specific issues detected by PMD."""
    report_path = pmd_report_txt_path
    code_style_count = 0

    remove_list = [
        "VariableNamingConventions",     # Meaningful variable names
        "FieldNamingConventions",       # Proper field names
        "MethodNamingConventions",      # Proper method names
        "ShortVariable",                # Flags overly short names
        "LongVariable",                 # Flags excessively long names
        "ExcessiveLengthRule",          # Enforces maximum line length
        "TooManyStatementsPerLine",     # Flags overly complex lines
        "AvoidFieldNameMatchingMethodName"  # Prevents name conflicts
    ]

    with open(report_path, "r") as f:
        lines = f.readlines()

    for line in lines:
        line = line.replace(
            rf"LLM-Improved-Code-Quality\test_data\temp\code\java\{file_name}", "")

        if "ParseException" in line:
            code_style_count = 1
            break

        if line.split("\t")[1].replace(":", "") in remove_list:
            code_style_count = 1
            break

    return [str(code_style_count)]


if __name__ == "__main__":

    cnt = 0

    for file_name in os.listdir("LLM-Improved-Code-Quality/test_data/temp/reports/python/flake8/"):
        if file_name.endswith(".txt"):
            flake8_path = "LLM-Improved-Code-Quality/test_data/temp/reports/python/flake8/" + file_name

            print(f"File: {file_name}")

            code_style_count = filter_python_flake8(
                flake8_path, file_name)  # working
            cnt += code_style_count

    for file_name in os.listdir("LLM-Improved-Code-Quality/test_data/temp/reports/python/pylint/"):
        if file_name.endswith(".txt"):
            pylint_path = "LLM-Improved-Code-Quality/test_data/temp/reports/python/pylint/" + file_name

            print(f"File: {file_name}")

            code_style_count = filter_python_pylint(
                pylint_path, file_name)  # working
            cnt += code_style_count

    for file_name in os.listdir("LLM-Improved-Code-Quality/test_data/temp/reports/java/pmd/"):
        if file_name.endswith(".txt"):
            pmd_path = "LLM-Improved-Code-Quality/test_data/temp/reports/java/pmd/" + file_name

            print(f"File: {file_name}")

            code_style_count = filter_java_pmd(
                pmd_path, file_name)  # working
            cnt += code_style_count

    for file_name in os.listdir("LLM-Improved-Code-Quality/test_data/temp/reports/java/checkstyle/"):
        if file_name.endswith(".txt"):
            checkstyle_path = "LLM-Improved-Code-Quality/test_data/temp/reports/java/checkstyle/" + file_name

            print(f"File: {file_name}")

            code_style_count = filter_java_checkstyle(
                checkstyle_path, file_name)  # working
            cnt += code_style_count

    print(cnt)

    # # Example to update the 'lines_of_code' column
    # file_path = "LLM-Improved-Code-Quality/test_data/temp/submissions/submission_results.xlsx"
    # column_name = "issues1"
    # column_data = cnt  # New data to be added to the existing column

    # update_existing_column_excel(file_path, column_name, column_data)
