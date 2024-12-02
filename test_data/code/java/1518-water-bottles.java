class Solution {
    public int numWaterBottles(int numBottles, int numExchange) {
        int totalBottles = numBottles;
        int emptyBottles = numBottles;
        
        while (emptyBottles >= numExchange) {
            int newFullBottles = emptyBottles / numExchange;
            totalBottles += newFullBottles;
            emptyBottles = newFullBottles + (emptyBottles % numExchange);
        }
        
        return totalBottles;
    }
}