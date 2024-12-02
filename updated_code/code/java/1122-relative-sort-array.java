import java.util.*;

public class Solution {
    public int[] relativeSortArray(int[] arr1, int[] arr2) {
        // Count frequency of elements in arr1
        Map<Integer, Integer> frequency = new HashMap<>();
        for (int num : arr1) {
            frequency.put(num, frequency.getOrDefault(num, 0) + 1);
        }

        // Initialize result array
        int[] result = new int[arr1.length];

        // Iterate through arr2
        int index = 0;
        for (int num : arr2) {
            while (frequency.get(num) > 0) {
                result[index++] = num;
                frequency.put(num, frequency.get(num) - 1);
            }
        }

        // Add remaining elements in ascending order
        for (Map.Entry<Integer, Integer> entry : frequency.entrySet()) {
            while (entry.getValue() > 0) {
                result[index++] = entry.getKey();
                entry.setValue(entry.getValue() - 1);
            }
        }

        // Return resulting array
        return Arrays.copyOfRange(result, 0, index);
    }
}