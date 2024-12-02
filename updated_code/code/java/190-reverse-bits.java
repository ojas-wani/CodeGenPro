/**
 * Reverse bits of a given 32 bits unsigned integer.
 *
 * @author Your Name
 */
public class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 32; i++) {
            sb.append(Integer.toString(n & 1));
            n >>= 1;
        }
        return Integer.parseInt(new StringBuilder(sb.reverse().toString()), 2);
    }
}