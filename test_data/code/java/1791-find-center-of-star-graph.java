class Solution {
    public int findCenter(int[][] edges) {
        int nodeCount = 0;
        int[] degree = new int[105];
        for (int[] edge : edges) {
            degree[edge[0] - 1]++;
            degree[edge[1] - 1]++;
        }
        for (int i = 0; i < degree.length; i++) {
            if (degree[i] == edges.length) {
                return i + 1;
            }
        }
        return -1; // Return -1 if the graph is not a star graph
    }
}