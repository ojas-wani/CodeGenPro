#!/usr/bin/env python
# coding: utf-8
# flake8: noqa
# pylint: enable=bad-whitespace
# pylint: enable=fixme

class PangramChecker:
    """Check if a sentence is a pangram."""

    def __init__(self):
        """Initialize the class."""
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"

    def check_if_pangram(self, sentence: str) -> bool:
        """Check if the sentence is a pangram.

        Args:
        sentence (str): The sentence to check.

        Returns:
        bool: True if the sentence is a pangram, False otherwise.
        """
        for char in self.alphabet:
            if char not in sentence:
                return False
        return True


if __name__ == "__main__":
    checker = PangramChecker()
    sentence = "thequickbrownfoxjumpsoverthelazydog"
    print(checker.check_if_pangram(sentence))  # Output: True

    sentence = "leetcode"
    print(checker.check_if_pangram(sentence))  # Output: False