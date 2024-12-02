class Solution {
    public int maximumPopulation(int[][] logs) {
        int[] count = new int[101]; // Initialize array with 101 elements
        for (int[] log : logs) {
            for (int year = log[0]; year < log[1]; year++) {
                count[year - 1950]++;
            }
        }
        int year = -1;
        int maxPopulation = 0;
        for (int i = 0; i < count.length; i++) {
            if (count[i] > maxPopulation) {
                maxPopulation = count[i];
                year = i + 1950; // Convert index to actual year
            }
        }
        return year;
    }
}