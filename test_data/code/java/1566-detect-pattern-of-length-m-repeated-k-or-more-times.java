class Solution {
    public boolean containsPattern(int[] arr, int m, int k) {
        if (arr.length < m * k) return false;
        
        for (int i = 0; i <= arr.length - m * k; i++) {
            if (i + m - 1 < arr.length && Arrays.equals(Arrays.copyOfRange(arr, i, i + m), Arrays.copyOfRange(arr, i + m, i + m * k))) {
                return true;
            }
        }
        return false;
    }
}