class Solution {
    public int maxNumberOfBalloons(String text) {
        int[] counts = new int[5];
        for (char c : text.toLowerCase().toCharArray()) {
            if (c == 'b') counts[0]++;
            else if (c == 'a') counts[1]++;
            else if (c == 'l') counts[2]++;
            else if (c == 'o') counts[3]++;
            else if (c == 'n') counts[4]++;
        }
        // "balloon" has 2 L's, 2 O's
        counts[2] /= 2;
        counts[3] /= 2;
        // find the min count of each character
        int minCount = Integer.MAX_VALUE;
        for (int count : counts) {
            minCount = Math.min(minCount, count);
        }
        return minCount;
    }
}