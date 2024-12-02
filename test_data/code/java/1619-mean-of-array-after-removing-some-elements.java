class Solution {
    public double trimMean(int[] arr) {
        Arrays.sort(arr);
        int len = arr.length;
        int count = (int) (len * 0.05);
        int sum = 0;
        for (int i = count; i < len - count; i++) {
            sum += arr[i];
        }
        return (double) sum / (len - 2 * count);
    }
}