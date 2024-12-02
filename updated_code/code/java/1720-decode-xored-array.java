import java.util.Arrays;

/**
 * Decode XORed Array
 */
public class Solution {
    /**
     * Decodes the XORed array.
     * 
     * @param encoded the XORed array
     * @param first the first element of the original array
     * @return the original array
     */
    public int[] decode(int[] encoded, int first) {
        int n = encoded.length + 1;
        int[] arr = new int[n];
        arr[0] = first;
        
        for (int i = 0; i < n - 1; i++) {
            arr[i + 1] = arr[i] ^ encoded[i];
        }
        return arr;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] encoded = {1, 2, 3};
        int first = 1;
        int[] result = solution.decode(encoded, first);
        System.out.println(Arrays.toString(result));
    }
}