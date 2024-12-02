package com.sample.java;

import java.util.Scanner;

/**
 * 
 * @author <Your Name>
 *
 */
public class Solution {
    public int subtractProductAndSum(int n) {
        int product = 1;
        int sum = 0;
        int temp = n;
        
        // Use Scanner to handle the possible large input
        Scanner scanner = new Scanner(String.valueOf(temp));
        
        while(scanner.hasNextInt()) {
            int digit = scanner.nextInt();
            product *= digit;
            sum += digit;
        }
        
        scanner.close();
        
        return product - sum;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int result = solution.subtractProductAndSum(234);
        System.out.print(result);
    }
}