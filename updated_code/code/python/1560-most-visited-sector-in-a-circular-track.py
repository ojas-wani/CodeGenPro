from typing import List

class Solution:
    """
    Docstring for the class
    """
    def most_visited(self, n: int, rounds: List[int]) -> List[int]:
        """
        Docstring for the method
        :param n: The number of sectors in the circular track
        :param rounds: The list of rounds in the marathon
        :return: A list of the most visited sectors
        """
        count = [0] * (n + 1)
        for i in range(1, len(rounds)):
            if rounds[i] > rounds[i - 1]:
                for j in range(rounds[i - 1] + 1, rounds[i]):
                    count[j % n] += 1
            else:
                for j in range(rounds[i - 1], rounds[i] + 1):
                    count[j % n] += 1
        return sorted([i for i, x in enumerate(count) if x == max(count)][1:])

if __name__ == '__main__':
    pass