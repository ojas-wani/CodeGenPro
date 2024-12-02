/**
 * This class provides an implementation of the method to find the bitwise XOR of all elements of an array.
 *
 * @author YourName
 */
package yourpackage;

import java.util.Arrays;

public class Solution {

    /**
     * This method calculates the bitwise XOR of all elements of an array.
     *
     * @param n     the number of elements in the array
     * @param start the starting value of the array
     * @return the bitwise XOR of all elements of the array
     */
    public int xorOperation(int n, int start) {
        int xor = 0;
        for (int i = 0; i < n; i++) {
            int num = start + 2 * i;
            xor ^= num;
        }
        return xor;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int n = 5;
        int start = 0;
        int result = solution.xorOperation(n, start);
        System.out.println("The bitwise XOR of all elements is " + result);
    }
}