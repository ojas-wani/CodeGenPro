import os
import pandas as pd
import numpy as np
import re


def filter_python_pylint(pylint_report_txt_path, file_name):
    """Filter Python code for specific issues detected by pylint."""
    report_path = pylint_report_txt_path
    return_lines = []

    remove_list = [
        "C0301", "C0305", "C0303", "C0304", "C0103", "C0112", "C0114", "C0115", "C0116",
        "C0410", "C0411", "C0412", "C0413", "C0414", "C0415", "R0903", "W0611", "W0401",
        "E0602", "W0621"
    ]

    with open(report_path, "r") as f:
        lines = f.readlines()

    if not lines:
        return []

    for line in lines:
        if line.startswith(file_name) and line.split(": ")[1] not in remove_list:
            return_lines.append("line " + ":".join(line.split(":")[1:]))

    return return_lines


def filter_python_flake8(flake8_report_txt_path, file_name):
    """Filter Python code for specific issues detected by flake8."""
    report_path = flake8_report_txt_path
    return_lines = []

    remove_list = [
        "F821", "W292", "E265", "E231", "W293", "E261", "E501", "E262", "W291", "E225",
        "E227", "E302", "E303", "E305", "E211", "E228", "E275", "E402", "E201", "E203"
    ]

    with open(report_path, "r") as f:
        lines = f.readlines()

    if not lines:
        return []

    for line in lines:
        line = line.replace(
            f"LLM-Improved-Code-Quality/test_data/temp2/updated_code/code/python/{file_name}.py", "")

        if line.split(" ")[1] not in remove_list:
            return_lines.append("line " + ":".join(line.split(":")[1:]))

    return return_lines


def filter_java_pmd(pmd_report_txt_path, file_name):
    """Filter Java code for specific issues detected by PMD."""
    report_path = pmd_report_txt_path
    return_lines = []

    remove_list = [
        "CommentRequired", "NoPackage", "AtLeastOneConstructor", "LocalVariableCouldBeFinal",
        "UseVarargs", "MethodArgumentCouldBeFinal", "ShortVariable", "OnlyOneReturn", "LawOfDemeter",
        "ControlStatementBraces", "CommentDefaultAccessModifier", "CommentSize", "AvoidLiteralsInIfCondition",
        "ImmutableField", "CognitiveComplexity", "CyclomaticComplexity", "FormalParameterNamingConventions",
        "UseUnderscoresInNumericLiterals", "AvoidReassigningLoopVariables", "ShortClassName", "AvoidInstantiatingObjectsInLoops",
        "OneDeclarationPerLine", "SystemPrintln", "LongVariable", "LocalVariableNamingConventions"
    ]

    if not os.path.exists(report_path):
        return []

    with open(report_path, "r") as f:
        lines = f.readlines()

    if not lines:
        return []

    for line in lines:
        line = line.replace(
            rf"LLM-Improved-Code-Quality\test_data\temp2\updated_code\code\java\{file_name}.java", "")

        if "ParseException" in line:
            break
            return_lines.append(line)
            return return_lines

        if line.split("\t")[1].replace(":", "") not in remove_list:
            return_lines.append("line " + ":".join(line.split(":")[1:]))

    return return_lines


def filter_java_checkstyle(checkstyle_report_txt_path, file_name):
    """Filter Java code for specific issues detected by Checkstyle."""
    report_path = checkstyle_report_txt_path
    return_lines = []

    remove_list = ["JavadocPackage", "NewlineAtEndOfFile", "WhitespaceAround", "WhitespaceAfter", "LineLength",    "RegexpSingleline", "JavadocVariable", "FinalParameters", "MagicNumber", "NeedBraces",    "NoWhitespaceBefore", "LocalVariableName", "OperatorWrap", "AvoidStarImport",
                   "InvalidJavadocPosition",    "NoWhitespaceAfter", "ParenPad", "MethodParamPad", "ParameterName", "LocalFinalVariableName",    "ConstantName", "MethodName", "StaticVariableName", "MemberName", "JavadocMethod", "MissingJavadocMethod",    "JavadocStyle", "DesignForExtension"]

    if not os.path.exists(report_path):
        return []

    with open(report_path, "r") as f:
        lines = f.readlines()

    if not lines:
        return []

    for line in lines:
        if line.startswith("[ERROR]"):
            line = line.replace("[ERROR] ", "")
            line = line.replace(
                rf"LLM-Improved-Code-Quality/test_data/temp2/updated_code/code/java/{file_name}.java", "")
            type_smell = line.split(". [")[1].replace("]", "").strip()

            if type_smell not in remove_list:
                return_lines.append("line " + ":".join(line.split(":")[2:]))

    return return_lines


if __name__ == "__main__":

    pylint_count = 0
    flake8_count = 0
    pmd_count = 0
    checkstyle_count = 0

    for file_name in os.listdir("LLM-Improved-Code-Quality/test_data/temp2/updated_code/code/python"):
        if file_name:
            file_name = file_name.split(".")[0] + ".txt"
            pylint_path = "LLM-Improved-Code-Quality/test_data/temp2/updated_code/reports/python/pylint/" + file_name
            flake8_path = "LLM-Improved-Code-Quality/test_data/temp2/updated_code/reports/python/flake8/" + file_name
            checkstyle_path = "LLM-Improved-Code-Quality/test_data/temp2/updated_code/reports/java/checkstyle/" + file_name
            pmd_path = "LLM-Improved-Code-Quality/test_data/temp2/updated_code/reports/java/pmd/" + file_name

            # print(filter_python_pylint(pylint_path, file_name)) # working
            # print(filter_python_flake8(flake8_path, file_name))  # working
            # print(filter_java_pmd(pmd_path, file_name))  # working
            # print(filter_java_checkstyle(checkstyle_path, file_name))  # working

            if filter_python_pylint(pylint_path, file_name) != []:
                pylint_count += 1
                print(f"File: {file_name}")
                print(filter_python_pylint(pylint_path, file_name))

            if filter_python_flake8(flake8_path, file_name) != []:
                flake8_count += 1
                print(f"File: {file_name}")
                print(filter_python_flake8(flake8_path, file_name))

            if filter_java_pmd(pmd_path, file_name) != []:
                pmd_count += 1
                print(f"File: {file_name}")
                print(filter_java_pmd(pmd_path, file_name))

            if filter_java_checkstyle(checkstyle_path, file_name) != []:
                checkstyle_count += 1
                print(f"File: {file_name}")
                print(filter_java_checkstyle(checkstyle_path, file_name))

    # path_report_pylint = "ChatGPT-CodeGenAnalysis-main/src/test_pylint/009-palindrome-number.txt"
    # path_report_flake8 = "ChatGPT-CodeGenAnalysis-main/src/test_flake8/009-palindrome-number.txt"
    # filter_python_pylint(path_report_pylint)
    # filter_python_flake8(path_report_flake8)
