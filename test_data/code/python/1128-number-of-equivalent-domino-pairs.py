class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = {}
        for domino in dominoes:
            domino.sort()  # sort the domino to make it unique
            count[tuple(domino)] = count.get(tuple(domino), 0) + 1
        pairs = 0
        for v in count.values():
            pairs += v * (v - 1) // 2  # calculate the number of pairs for each unique domino
        return pairs