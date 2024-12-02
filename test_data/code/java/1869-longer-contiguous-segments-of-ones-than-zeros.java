class Solution {
    public boolean checkZeroOnes(String s) {
        int maxOnes = 0, maxZeros = 0, currentOnes = 0, currentZeros = 0;
        
        for (char c : s.toCharArray()) {
            if (c == '1') {
                currentOnes++;
                maxOnes = Math.max(maxOnes, currentOnes);
                currentZeros = 0;
            } else {
                currentZeros++;
                maxZeros = Math.max(maxZeros, currentZeros);
                currentOnes = 0;
            }
        }
        
        return maxOnes > maxZeros;
    }
}