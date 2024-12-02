from typing import List

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        """
        This function calculates the number of pairs of dominoes in a given list that are equivalent.

        Args:
            dominoes (List[List[int]]): A list of dominoes, where each domino is a list of two integers.

        Returns:
            int: The number of pairs of dominoes that are equivalent.
        """
        count = {}
        for domino in dominoes:
            # sort the domino to make it unique
            domino.sort()
            # count the frequency of each domino
            count[tuple(domino)] = count.get(tuple(domino), 0) + 1
        pairs = 0
        for v in count.values():
            # calculate the number of pairs for each unique domino
            pairs += v * (v - 1) // 2
        return pairs

    from typing import List

    class Solution:
        def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:

    class Solution:
        """
        This class contains a method to calculate the number of pairs of dominoes in a given list that are equivalent.
        """

        def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
            """
            This function calculates the number of pairs of dominoes in a given list that are equivalent.

            Args:
                dominoes (List[List[int]]): A list of dominoes, where each domino is a list of two integers.

            Returns:
                int: The number of pairs of dominoes that are equivalent.
            """
    
    def num_equiv_domino_pairs(self, dominoes):
    
    from typing import List
    
    pairs += v * (v - 1) // 2
    
    return pairs
    # This is the last line of the code. Adding a newline now.
    
    return pairs
    # This is the last line of the code. Adding a newline.
    
    """
    This module contains a class to calculate the number of pairs of dominoes in a given list that are equivalent.
    """
    class Solution:
        """
        This class contains a method to calculate the number of pairs of dominoes in a given list that are equivalent.
        """
    
    def num_equiv_domino_pairs(self, dominoes: List[List[int]]) -> int:
        """
        This function calculates the number of pairs of dominoes in a given list that are equivalent.

        Args:
            dominoes (List[List[int]]): A list of dominoes, where each domino is a list of two integers.

        Returns:
            int: The number of pairs of dominoes that are equivalent.
        """