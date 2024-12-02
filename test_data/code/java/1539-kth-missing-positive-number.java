class Solution {
    public int findKthPositive(int[] arr, int k) {
        int missingCount = 0;
        int currentNumber = 1;
        
        while (true) {
            if (Arrays.binarySearch(arr, currentNumber) < 0) {
                missingCount++;
                if (missingCount == k) {
                    return currentNumber;
                }
            }
            currentNumber++;
        }
    }
}