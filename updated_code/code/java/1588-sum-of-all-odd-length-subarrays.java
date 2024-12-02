import java.util.Arrays;

/**
 * Class that calculates the sum of all possible odd-length subarrays of a given array.
 */
public class SumOfAllOddLengthSubarrays {

    /**
     * Method that calculates the sum of all possible odd-length subarrays of a given array.
     *
     * @param arr The input array.
     * @return The sum of all possible odd-length subarrays.
     */
    public int sumOddLengthSubarrays(int[] arr) {
        int n = arr.length;
        int totalSum = 0;

        // Use varargs for methods or constructors which take an array as the last parameter
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                if ((j - i + 1) % 2 != 0) {
                    totalSum += Arrays.stream(arr, i, j + 1).sum();
                }
            }
        }

        return totalSum;
    }

    public static void main(String[] args) {
        SumOfAllOddLengthSubarrays solver = new SumOfAllOddLengthSubarrays();
        int[] arr = {1, 4, 2, 5, 3};
        int result = solver.sumOddLengthSubarrays(arr);
        System.out.println(result);  // Output: 58
    }
}