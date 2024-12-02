/**
 * Package: Solution
 * Description: This class contains a solution to the problem of minimum cost to move chips to the same position.
 */
package solution;

/**
 * Class: Solution
 * Description: This class provides a solution to the problem of minimum cost to move chips to the same position.
 */
public class Solution {
    /**
     * Method: minCostToMoveChips(int[])
     * Description: This method calculates the minimum cost to move all the chips to the same position.
     * @param position: An array of integers representing the positions of the chips.
     * @return: An integer representing the minimum cost to move all the chips to the same position.
     */
    public int minCostToMoveChips(int[] position) {
        // Initialize an array to count the number of chips at each position (0 or 1).
        int[] counts = new int[2];
        // Iterate through each chip position.
        for (int pos : position) {
            // Count the number of chips at position 0 and position 1.
            counts[pos % 2]++;
        }
        // Return the minimum cost, which is the minimum number of chips at positions 0 and 1.
        return Math.min(counts[0], counts[1]);
    }
}