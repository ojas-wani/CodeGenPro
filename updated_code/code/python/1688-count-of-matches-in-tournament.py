py
# Missing-module-docstring
import unittest

class MatchCountTournament:
    """
    Class for calculating the number of matches in a tournament.
    """
    def __init__(self):
        """
        Initialize the class.
        """

    def count_matches(self, teams: int) -> int:
        """
        Calculate the number of matches played in the tournament until a winner is decided.
        
        Args:
        teams (int): The number of teams in the tournament.
        
        Returns:
        int: The number of matches played in the tournament.
        """
        total_matches = 0
        while teams > 1:
            if teams % 2 == 0:
                total_matches += teams // 2
                teams = teams // 2
            else:
                total_matches += (teams - 1) // 2
                teams = (teams - 1) // 2 + 1
        return total_matches