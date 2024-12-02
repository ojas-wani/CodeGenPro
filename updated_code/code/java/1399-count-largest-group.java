/**
 * Package: Programming
 * Description: Count the largest group that sums to equal the digits of their numbers
 *
 * @author [Your Name]
 * @version 1.0
 */
package Programming;

import java.util.Arrays;

public class Solution {
    /**
     * Count the largest group that sums to equal the digits of their numbers
     *
     * @param n the input integer
     * @return the number of groups that have the largest size
     */
    public int countLargestGroup(int n) {
        int[] count = new int[37];
        int max = 0;
        for (int i = 1; i <= n; i++) {
            int sum = 0;
            for (char c : Integer.toString(i).toCharArray()) {
                sum += c - '0';
            }
            count[sum]++;
            max = Math.max(max, count[sum]);
        }
        return Arrays.stream(count).filter(x -> x == max).count();
    }
}