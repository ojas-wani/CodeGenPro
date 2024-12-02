class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        emptyBottles = numBottles
        fullBottles = numBottles
        totalBottles = fullBottles
        while emptyBottles >= numExchange:
            newFullBottles = emptyBottles // numExchange
            emptyBottles = emptyBottles % numExchange + newFullBottles
            fullBottles += newFullBottles
            totalBottles += newFullBottles
        return totalBottles