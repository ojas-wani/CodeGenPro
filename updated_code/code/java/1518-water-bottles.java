package LLMImprovedCodeQuality;

/**
 * This class is designed to calculate the maximum number of water bottles that can be drunk.
 */
public class Solution {
    /**
     * This method calculates the maximum number of water bottles that can be drunk.
     *
     * @param numBottles The initial number of water bottles.
     * @param numExchange The number of empty water bottles that can be exchanged for a full water bottle.
     * @return The maximum number of water bottles that can be drunk.
     */
    public int numWaterBottles(int numBottles, int numExchange) {
        int totalBottles = numBottles;
        int emptyBottles = numBottles;
        
        while (emptyBottles >= numExchange) {
            final int newFullBottles = emptyBottles / numExchange;
            totalBottles += newFullBottles;
            emptyBottles = newFullBottles + (emptyBottles % numExchange);
        }
        
        return totalBottles;
    }
}