import java.util.*;

class Solution {
    public List<Integer> mostVisited(int n, int[] rounds) {
        List<Integer> res = new ArrayList<>();
        int maxCount = 0;

        // To store the count of visit for each sector
        int[] count = new int[n + 1];

        // Loop for each round
        for (int i = 1; i <= rounds.length; i++) {
            // Calculate the sector number for this round according to the circular index
            int start = rounds[i - 1];
            int end = rounds[i];

            // If the start sector is less than the end sector, it means that the sectores from start to n and then from 1 to end will be visited
            if (start < end) {
                for (int j = start; j <= n; j++) {
                    count[j]++;
                }
                for (int j = 1; j <= end; j++) {
                    count[j]++;
                }
            } else if (start > end) {
                // If the start sector is greater than the end sector, it means that the sectors from start to n will be visited at the end of the marathon
                for (int j = start; j <= n; j++) {
                    count[j]++;
                }
                // The sectors from 1 to end are visited at the start of the marathon
                for (int j = 1; j <= end; j++) {
                    count[j]++;
                }
            } else {
                // If the start sector is equal to the end sector, it means that the sectors from start to end are visited
                for (int j = start; j <= end; j++) {
                    count[j]++;
                }
            }

            // Update the maximum count
            for (int j = 1; j <= n; j++) {
                if (count[j] > maxCount) {
                    maxCount = count[j];
                    res.clear();
                    res.add(j);
                } else if (count[j] == maxCount) {
                    res.add(j);
                }
            }
        }

        // Sort the result in ascending order
        Collections.sort(res);

        return res;
    }
}