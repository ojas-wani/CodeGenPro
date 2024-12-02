/**
 * Author: [Your Name]
 */
package com.app.packages;

public class CheckOnesSegment {
    public boolean checkOnesSegment(String binaryString) {
        boolean hasOnesSegment = false;
        
        for (int i = 0; i < binaryString.length(); i++) {
            if (binaryString.charAt(i) == '1') {
                if (hasOnesSegment) {
                    return false;
                }
                hasOnesSegment = true;
            }
        }
        return true;
    }
}