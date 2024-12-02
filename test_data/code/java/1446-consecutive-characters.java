class Solution {
    public int maxPower(String s) {
        int maxPower = 0;
        char currentChar = s.charAt(0);
        int currentCount = 1;
        
        for (int i = 1; i < s.length(); i++) {
            if (s.charAt(i) == currentChar) {
                currentCount++;
            } else {
                maxPower = Math.max(maxPower, currentCount);
                currentChar = s.charAt(i);
                currentCount = 1;
            }
        }
        
        return Math.max(maxPower, currentCount);
    }
}