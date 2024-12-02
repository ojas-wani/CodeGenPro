class Solution:
    def is_sum_equal(self, first_word: str, second_word: str, target_word: str) -> bool:
        """
        This method checks if the sum of the numerical values of two words equals the numerical value of a target word.

        Args:
            first_word (str): The first word.
            second_word (str): The second word.
            target_word (str): The target word.

        Returns:
            bool: True if the sum of the numerical values of the two words equals the numerical value of the target word, False otherwise.
        """
        def get_numerical_value(word: str) -> int:
            """
            This method calculates the numerical value of a word.

            Args:
                word (str): The word.

            Returns:
                int: The numerical value of the word.
            """
            return int(''.join(str(ord(c) - ord('a')) for c in word))

        return get_numerical_value(first_word) + get_numerical_value(second_word) == get_numerical_value(target_word)