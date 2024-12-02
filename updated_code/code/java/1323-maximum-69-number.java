/**
 * Package: WhateverpackageNameYouWant;
 * 
 * Description: This class implements the function to find the maximum number 
 *              by changing at most one digit '6' to '9' in the given integer.
 * 
 * @author YourName
 */
package WhateverpackageNameYouWant;

import java.util.Scanner;

public class Solution {
    /**
     * Method to find the maximum number by changing at most one digit '6' to '9' in the given integer.
     * 
     * @param num The input integer to find the maximum number.
     * @return The maximum number by changing at most one digit '6' to '9' in the given integer.
     */
    public int maximum69Number(int num) {
        String str = String.valueOf(num);
        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i) == '6') {
                str = str.substring(0, i) + '9' + str.substring(i + 1);
                break;
            }
        }
        return Integer.parseInt(str);
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        int num = 9996;
        System.out.println(sol.maximum69Number(num));
    }
}