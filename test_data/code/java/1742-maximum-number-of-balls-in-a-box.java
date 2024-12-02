class Solution {
    public int countBalls(int lowLimit, int highLimit) {
        int[] count = new int[76]; // boxes from 1 to 75
        for (int i = lowLimit; i <= highLimit; i++) {
            int sum = 0;
            int j = i;
            while (j != 0) {
                sum += j % 10;
                j /= 10;
            }
            count[sum]++;
        }
        int max = 0;
        for (int i = 1; i < count.length; i++) {
            if (count[i] > max) {
                max = count[i];
            }
        }
        return max;
    }
}