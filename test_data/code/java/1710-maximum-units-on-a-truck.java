class Solution {
    public int maximumUnits(int[][] boxTypes, int truckSize) {
        Arrays.sort(boxTypes, (a, b) -> b[1] - a[1]);
        int totalUnits = 0;
        
        for (int[] boxes : boxTypes) {
            int boxesToTake = Math.min(truckSize, boxes[0]);
            totalUnits += boxesToTake * boxes[1];
            truckSize -= boxesToTake;
            if (truckSize == 0) break;
        }
        
        return totalUnits;
    }
}