class Solution {
    public int maxScore(String s) {
        int max = 0;
        for (int i = 1; i < s.length() - 1; i++) {
            int leftOnes = 0, rightZeros = 0;
            for (int j = 0; j < i; j++) {
                if (s.charAt(j) == '1') {
                    leftOnes++;
                }
            }
            for (int k = i; k < s.length(); k++) {
                if (s.charAt(k) == '0') {
                    rightZeros++;
                }
            }
            max = Math.max(max, leftOnes + rightZeros);
        }
        return max;
    }
}