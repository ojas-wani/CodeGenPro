from typing import List

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        """
        Given two arrays of integers `nums` and `index`. 
        Create _target_ array under the following rules:
        * Initially _target_ array is empty.
        * From left to right read nums[i] and index[i], 
          insert at index `index[i]` the value `nums[i]` in _target_ array.
        * Repeat the previous step until there are no elements to read in `nums` and `index`.
        Return the _target_ array.
        """
        target = []  # Initially _target_ array is empty.
        for num, i in zip(nums, index):
            target.insert(i, num)
        return target

LLM-Improved-Code-Quality/test_data/temp2/code/python/1389-create-target-array-in-the-given-order.py:1:1: E302 expected 2 blank lines, found 0
LLM-Improved-Code-Quality/test_data/temp2/code/python/1389-create-target-array-in-the-given-order.py:6:0: E302 expected 2 blank lines, found 0

************* Module 1389-create-target-array-in-the-given-order
1389-create-target-array-in-the-given-order.py:2:0: C0115: Missing class docstring (missing-class-docstring)
1389-create-target-array-in-the-given-order.py:4:4: C0116: Missing function or method docstring (missing-function-docstring)
1389-create-target-array-in-the-given-order.py:8:0: C0304: Final newline missing (missing-final-newline)