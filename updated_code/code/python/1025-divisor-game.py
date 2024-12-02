Python
class Solution:
    def divisorGame(self, n: int) -> bool:
        players = [False] * (n + 1)
        for i in range(2, n + 1):
            players[i] = not any(j > 0 and i % j == 0 for j in range(1, i))
        return players[n]