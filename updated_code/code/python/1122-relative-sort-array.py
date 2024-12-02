import typing

class Solution:
    """
    This class provides a method to sort the elements of `arr1` such that the relative ordering of items in `arr1`
    are the same as in `arr2`. Elements that do not appear in `arr2` should be placed at the end of `arr1` in **ascending** order.
    """
    def relativeSortArray(self, arr1: typing.List[int], arr2: typing.List[int]) -> typing.List[int]:
        """
        This method takes two lists of integers as input, `arr1` and `arr2`, and returns a sorted list of integers.

        :param arr1: The input list of integers
        :param arr2: The list of integers that appear in `arr1` in a specific order
        :return: A sorted list of integers where elements that appear in `arr2` are in the same relative order,
                 and elements that do not appear in `arr2` are at the end in ascending order
        """
        count_map = {}
        for num in arr1:
            if num in count_map:
                count_map[num] += 1
            else:
                count_map[num] = 1
        
        sorted_output = []
        for num in arr2:
            if num in count_map:
                sorted_output.extend([num] * count_map[num])
                del count_map[num]
        
        for num in sorted(count_map.keys()):
            sorted_output.extend([num] * count_map[num])
        
        return sorted_output