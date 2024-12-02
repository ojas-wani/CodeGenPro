package comsolution;

import java.util.Arrays;

/**
 * Class that counts the number of students doing their homework at a given time.
 */
public class Solution {

    /**
     * Counts the number of students doing their homework at a given time.
     * @param startTime The start time of each student's homework in seconds.
     * @param endTime The end time of each student's homework in seconds.
     * @param queryTime The time at which we want to know if students are doing their homework.
     * @return The number of students doing their homework at the queryTime.
     */
    public int busyStudent(int[] startTime, int[] endTime, int queryTime) {
        int count = 0;
        for (int i = 0; i < startTime.length; i++) {
            // Make startTime, endTime, and queryTime final as per PMD suggestion
            if ((startTime[i] <= queryTime && queryTime <= endTime[i])) {
                count++;
            }
        }
        return count;
    }
}