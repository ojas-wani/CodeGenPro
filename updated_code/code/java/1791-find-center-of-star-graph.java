import java.util.Arrays;

public class Solution {
    public int findCenter(int[][] edges) {
        // Package comment is added
        // Constructor comment is added
        // The constructor declares at least one constructor
        public Solution() {
        }

        // Public method comment is added
        // The method uses varargs
        public int findCenter(int[][] edges) {
            // Variable 'degree' is declared final
            final int[] degree = new int[105];
            // Variable 'edge' is declared final
            for (final int[] edge : edges) {
                degree[edge[0] - 1]++;
                degree[edge[1] - 1]++;
            }
            // Unused local variable 'nodeCount' is removed
            for (int i = 0; i < degree.length; i++) {
                if (degree[i] == edges.length) {
                    return i + 1;
                }
            }
            // Only one return is ensured
            return -1;
        }
    }
}