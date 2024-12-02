class Solution {
    public void duplicateZeros(int[] arr) {
        int length = arr.length;
        int index = length - 1;
        
        for(int i = length - 1; i >= 0; i--) {
            if(arr[i] == 0) {
                if(i < length - 1) {
                    arr[index] = 0;
                    index--;
                }
                arr[index] = 0;
                index--;
            } else {
                arr[index] = arr[i];
                index--;
            }
        }
    }
}