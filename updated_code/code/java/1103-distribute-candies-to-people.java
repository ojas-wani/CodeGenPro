// Add package declaration
package com.example;

/**
 * Class to distribute candies to people.
 */
public class Solution {

    /**
     * Distribute candies to people.
     * 
     * @param candies the total number of candies
     * @param numPeople the number of people
     * @return the distribution of candies
     */
    public int[] distributeCandies(int candies, int numPeople) {
        int[] ans = new int[numPeople];
        int person = 0;
        int given = 0;

        // Add a comment to explain the logic
        while (candies > 0) {
            // Calculate the number of candies to give
            int toGive = Math.min(candies, person + 1);
            ans[person] += toGive;
            // Update the remaining candies
            candies -= toGive;
            // Move to the next person
            person = (person + 1) % numPeople;
        }
        return ans;
    }
}