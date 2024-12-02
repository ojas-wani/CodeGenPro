package solution;

import java.util.Arrays;

public class Solution {
    
    public double average(int[] salary) {
        // Calculate sum, min and max
        int sum = 0;
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;
        
        for (int i : salary) {
            sum += i;
            if (i < min) {
                min = i;
            } else if (i > max) {
                max = i;
            }
        }
        
        // Calculate average
        return (double) (sum - min - max) / (salary.length - 2);
    }    
}