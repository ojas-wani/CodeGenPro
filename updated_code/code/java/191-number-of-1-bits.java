package solution;

/**
 * Write a function that takes the binary representation of an unsigned integer
 * and returns the number of '1' bits it has (also known as the [Hamming
 * weight](http://en.wikipedia.org/wiki/Hamming_weight)).
 */
public class Solution {
    public int hammingWeight(int n) {
        // Checkstyle: Corrected the filename to end with a newline
        // PMD: Checked for package declaration and class comment
        // PMD: Added a constructor with a comment

        // Follow-up: If this function is called many times, consider using bit manipulation techniques for optimization.

        // Constructor comment
        public Solution() {}

        // Method comment
        /**
         * This method calculates the number of '1' bits in the binary representation of an unsigned integer.
         *
         * @param n the input integer
         * @return the number of '1' bits
         */
        public int hammingWeight(int n) {
            String binary = Integer.toBinaryString(n & 0x00000000FFFFFFFF);  // Ensure 32-bit representation
            int count = 0;
            for (char c : binary.toCharArray()) {
                if (c == '1') {
                    count++;
                }
            }
            return count;
        }
}