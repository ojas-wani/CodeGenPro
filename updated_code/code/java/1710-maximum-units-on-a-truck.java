package org.test.pkg;

import java.util.Arrays;

public class Solution {

    /**
     * You are assigned to put some amount of boxes onto **one truck**. 
     * You are given a 2D array `boxTypes`, where `boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]`:
     *   - `numberOfBoxesi` is the number of boxes of type `i`.
     *   - `numberOfUnitsPerBoxi` is the number of units in each box of the type `i`.
     * 
     * @param boxTypes a 2D array representing the boxes
     * @param truckSize the maximum number of boxes that can be put on the truck
     * @return the maximum total number of units that can be put on the truck
     */
    public int maximumUnits(int[][] boxTypes, int truckSize) {
        // Sort the boxes by the number of units per box in descending order
        Arrays.sort(boxTypes, (a, b) -> Integer.compare(b[1], a[1]));
        
        int totalUnits = 0;
        
        for (int[] boxes : boxTypes) {
            final int boxesToTake = Math.min(truckSize, boxes[0]);
            totalUnits += boxesToTake * boxes[1];
            truckSize -= boxesToTake;
            if (truckSize == 0) break;
        }
        
        return totalUnits;
    }
}