/** Package: com.example.palindromechecker */

import java.io.*;

class Solution {
    public boolean isPalindrome(int x) {
        // Check if x is negative
        if (x < 0) {
            return false;
        }

        int reversed = 0;
        // Declare 'original' as final
        final int original = x;
        while (x > 0) {
            // Declare 'remainder' as final
            final int remainder = x % 10;
            reversed = reversed * 10 + remainder;
            x = x / 10;
        }
        // Return the result
        return original == reversed;
    }
}