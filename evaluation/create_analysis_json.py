import os
import json
import re
import glob
from filter_analysis_results import filter_python_pylint, filter_python_flake8, filter_java_pmd, filter_java_checkstyle

if __name__ == "__main__":

    analysis_json = []  # dictionary to store the analysis results

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

            pylint_value = filter_python_pylint(pylint_path, file_name)
            flake8_value = filter_python_flake8(flake8_path, file_name)
            pmd_value = filter_java_pmd(pmd_path, file_name)
            checkstyle_value = filter_java_checkstyle(
                checkstyle_path, file_name)

            if filter_python_pylint(pylint_path, file_name) != []:
                pylint_count += 1

            if filter_python_flake8(flake8_path, file_name) != []:
                flake8_count += 1

            if filter_java_pmd(pmd_path, file_name) != []:
                pmd_count += 1

            if filter_java_checkstyle(checkstyle_path, file_name) != []:
                checkstyle_count += 1

            analysis_json.append({'file_name': file_name, 'flake8': flake8_value,
                                 'pylint': pylint_value, 'pmd': pmd_value, 'checkstyle': checkstyle_value})

    with open(r"LLM-Improved-Code-Quality\test_data\temp2\updated_code\reports\analysis.json", 'w') as f:
        json.dump(analysis_json, f)
    
    print(f"Total files with pylint issues: {pylint_count}")
    print(f"Total files with flake8 issues: {flake8_count}")
    print(f"Total files with pmd issues: {pmd_count}")
    print(f"Total files with checkstyle issues: {checkstyle_count}")
