class Solution {
    public int minCostToMoveChips(int[] position) {
        int[] counts = new int[2];
        for (int pos : position) {
            counts[pos % 2]++;
        }
        return Math.min(counts[0], counts[1]);
    }
}