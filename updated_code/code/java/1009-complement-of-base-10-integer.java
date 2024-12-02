/**
 * Solution class that finds the bitwise complement of a given integer.
 *
 * @author <Your Name>
 */
public class Solution {
    /**
     * Returns the bitwise complement of the given integer {@code n}.
     *
     * @param n the given integer
     * @return the bitwise complement of {@code n}
     */
    public int bitwiseComplement(int n) {
        // Return the bitwise complement of the given integer
        int res = 0;
        int max = 0;
        while (max <= n) {
            max <<= 1;
        }
        max >>= 1;
        while (n > 0) {
            res <<= 1;
            if ((n & 1) == 0) {
                res |= 1;
            }
            n >>= 1;
        }
        return res;
    }
}