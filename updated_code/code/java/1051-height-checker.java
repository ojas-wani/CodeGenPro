package comSolution;
/**
 * This class provides a solution to the problem of counting the number of 
 * indices where the heights[i] is not equal to expected[i] in the given array.
 */
public class Solution {
    /**
     * This method takes an integer array heights as input, sorts it in non-decreasing order, 
     * and then counts the number of indices where heights[i] is not equal to expected[i].
     * 
     * @param heights The input array of integers representing the current order of 
     *                the students standing in a line.
     * @return The number of indices where the heights[i] is not equal to expected[i].
     */
    public int heightChecker(int[] heights) {
        int[] sortedHeights = heights.clone();
        Arrays.sort(sortedHeights);
        
        int count = 0;
        for (int i = 0; i < heights.length; i++) {
            if (heights[i] != sortedHeights[i]) {
                count++;
            }
        }
        
        return count;
    }
}