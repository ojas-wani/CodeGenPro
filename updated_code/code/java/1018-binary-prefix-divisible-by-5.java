/**
 * Description: This class solves the issue "binary prefix divisible by 5".
 * 
 * @author Your Name
 */
package com ISSUE;

import java.util.ArrayList;
import java.util.List;

public class BinaryPrefixDivisibleBy5 {
    /**
     * This method determines whether each binary prefix is divisible by 5 or not.
     * 
     * @param nums a binary array
     * @return a list of boolean values, where each value corresponds to whether the respective binary prefix is divisible by 5 or not
     */
    public List<Boolean> prefixesDivBy5(int[] nums) {
        List<Boolean> answer = new ArrayList<>();
        int sum = 0;
        for (final int num : nums) { // Declare the variable 'num' as final
            sum = (sum * 2 + num) % 5; // Avoid using magic numbers
            answer.add(sum == 0);
        }
        return answer;
    }
}