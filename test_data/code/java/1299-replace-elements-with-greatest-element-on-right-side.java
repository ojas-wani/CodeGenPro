class Solution {
    public int[] replaceElements(int[] arr) {
        int n = arr.length;
        if (n == 0) {
            return new int[0];
        }
        
        int max = arr[n - 1];
        arr[n - 1] = -1;
        
        for (int i = n - 2; i >= 0; i--) {
            if (arr[i] > max) {
                max = arr[i];
            }
            arr[i] = max;
        }
        
        return arr;
    }
}