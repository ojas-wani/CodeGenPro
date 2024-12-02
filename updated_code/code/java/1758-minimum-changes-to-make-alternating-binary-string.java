package llmImprovedCodeQuality;

/**
 * Class to solve issues based on description and reports.
 */
public class MinOperations {
    /**
     * Method to find the minimum operations needed to make the string alternating.
     * @param s the input string
     * @return the minimum operations needed
     */
    public int minOperations(String s) {
        int count = 0;
        char prev = s.charAt(0);
        for (int i = 1; i < s.length(); i++) {
            if (s.charAt(i) == prev) {
                count++;
            }
            prev = s.charAt(i);
        }
        return count;
    }
}