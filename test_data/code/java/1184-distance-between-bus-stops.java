class Solution {
    public int distanceBetweenBusStops(int[] distance, int start, int destination) {
        int total = 0;
        int min = Integer.MAX_VALUE;
        for (int i = 1; i < distance.length; i++) {
            total += distance[i];
            min = Math.min(min, distance[i]);
        }
        total += distance[0];
        total = Math.min(total, total - (distance[destination] + total - distance[start]));
        return Math.min(total, total - min);
    }
}