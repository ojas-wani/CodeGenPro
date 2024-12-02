class Solution {
    public boolean canThreePartsEqualSum(int[] arr) {
        int sum = 0;
        for(int i = 0; i < arr.length; i++) {
            sum += arr[i];
        }
        
        if(sum % 3 != 0) {
            return false;
        }
        
        int targetSum = sum / 3;
        int count = 0;
        int currentSum = 0;
        for(int i = 0; i < arr.length; i++) {
            currentSum += arr[i];
            if(currentSum == targetSum) {
                count++;
                currentSum = 0;
            }
        }
        return count >= 2;
    }
}