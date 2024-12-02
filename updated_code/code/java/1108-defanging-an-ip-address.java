package com.issues;

import java.util.Scanner;

/**
 * Defang an IP address, replace every period with [.].
 */
public class Solution {
    /**
     * Defang an IP address, replace every period with [.].
     * 
     * @param address the IP address to be defanged
     * @return the defanged IP address
     */
    public String defangIPaddr(String address) {
        return address.replace(".", "[.]");
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter an IP address:");
        String address = scanner.nextLine();
        System.out.println("Defanged IP address: " + solution.defangIPaddr(address));
    }
}