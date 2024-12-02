import java.util.Arrays;
import java.lang.System;

public class Solution {
    public String sortString(String s) {
        // Comment added as required by PMD
        // The problem statement is to reorder the string using the given algorithm
        // The code below sorts the string first and then reorders it according to the problem statement's rules
        char[] arr = s.toCharArray();
        Arrays.sort(arr);

        StringBuilder result = new StringBuilder();
        int left = 0, right = arr.length - 1;

        // The while loop iterates until all characters are added to the result
        while (left <= right) {
            // If the left index is less than or equal to the right index, we can pick the smallest character
            if (left <= right) {
                result.append(arr[left]);
                left++;
            }

            // If the left index is less than or equal to the right index, we can pick the smallest character greater than the last appended character
            if (left <= right) {
                result.append(arr[right]);
                right--;
            }
        }

        // Return the result
        return result.toString();
    }
}