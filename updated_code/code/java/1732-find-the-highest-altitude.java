/**
 * This class provides a solution for the "Find the Highest Altitude" problem.
 *
 * @author Your Name
 */
public class Solution {
    /**
     * This method calculates the highest altitude for a given set of gain values.
     * 
     * @param gain an integer array representing the net gain in altitude between points.
     * @return the highest altitude of a point.
     */
    public int largestAltitude(int[] gain) {
        int maxAltitude = 0;
        int currentAltitude = 0;
        for (final int heightGain : gain) {
            currentAltitude += heightGain;
            maxAltitude = Math.max(maxAltitude, currentAltitude);
        }
        return maxAltitude;
    }
}