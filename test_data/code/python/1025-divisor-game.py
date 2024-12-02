Python
class Solution:
    def divisorGame(self, n: int) -> bool:
        players = [True] * (n + 1)
        players[1] = False
        for i in range(2, n + 1):
            for j in range(2, i):
                if i % j == 0 and not players[i - j]:
                    players[i] = False
                    break
        return players[n]