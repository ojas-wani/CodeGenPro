class Solution {
    public int findSpecialInteger(int[] arr) {
        int n = arr.length;
        int targetCount = (int)Math.ceil(n * 0.25);
        for (int i = 0; i < n; i++) {
            int count = 1;
            for (int j = i + 1; j < n; j++) {
                if (arr[i] == arr[j]) {
                    count++;
                } else {
                    break;
                }
            }
            if (count >= targetCount) {
                return arr[i];
            }
        }
        return -1;
    }
}