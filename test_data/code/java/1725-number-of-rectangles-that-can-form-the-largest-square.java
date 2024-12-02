class Solution {
    public int countGoodRectangles(int[][] rectangles) {
        int maxLen = 0, count = 0;
        for (int[] rectangle : rectangles) {
            int length = Math.min(rectangle[0], rectangle[1]);
            if (length > maxLen) {
                maxLen = length;
                count = 1;
            } else if (length == maxLen) {
                count++;
            }
        }
        return count;
    }
}