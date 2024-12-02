class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        count = [0] * (n + 1)
        for i in range(1, len(rounds)):
            if rounds[i] > rounds[i - 1]:
                for j in range(rounds[i - 1], rounds[i]):
                    count[j] += 1
            else:
                for j in range(rounds[i - 1], rounds[i] + 1):
                    count[j] += 1
        return sorted([i for i, x in enumerate(count) if x == max(count)][1:])