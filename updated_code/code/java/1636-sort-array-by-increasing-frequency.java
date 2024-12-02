/**
 * @author Your Name
 * @version 1.0
 */
package JavaAssignments;
import java.util.*;

public class Solution {
    public int[] frequencySort(int[] nums) {
        // Check and handle null input
        if (nums == null) {
            return null;
        }

        // Check and handle empty array
        if (nums.length == 0) {
            return new int[0];
        }

        // Create a frequency map
        Map<Integer, Integer> frequencyMap = new HashMap<>();
        for (int num : nums) {
            frequencyMap.put(num, frequencyMap.getOrDefault(num, 0) + 1);
        }

        // Create a list to store the sorted indices
        List<Integer> sortedIndices = new ArrayList<>();

        // Iterate over the frequency map and add each number to the list the number of times it appears in the array
        for (Map.Entry<Integer, Integer> entry : frequencyMap.entrySet()) {
            for (int i = 0; i < entry.getValue(); i++) {
                sortedIndices.add(entry.getKey());
            }
        }

        // Sort the list in decreasing order of frequency, and then in increasing order
        Collections.sort(sortedIndices, (a, b) -> {
            if (Collections.frequency(Arrays.asList(nums), a) == Collections.frequency(Arrays.asList(nums), b)) {
                return Integer.compare(b, a);
            } else {
                return Integer.compare(Collections.frequency(Arrays.asList(nums), a), Collections.frequency(Arrays.asList(nums), b));
            }
        });

        // Create an array to store the sorted numbers
        int[] result = new int[nums.length];

        // Assign the sorted indices to the array
        int index = 0;
        for (int num : sortedIndices) {
            result[index++] = num;
        }

        // Return the sorted array
        return result;
    }
}