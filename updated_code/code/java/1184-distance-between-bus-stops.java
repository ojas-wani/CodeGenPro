package assignments;

import java.util.Arrays;

/**
 * This class is used to find the distance between bus stops.
 */
public class DistanceBetweenBusStops {
    /**
     * This method finds the shortest distance between two bus stops.
     * 
     * @param distance         The array of distances between adjacent bus stops.
     * @param start            The starting bus stop.
     * @param destination      The destination bus stop.
     * @return                 The shortest distance between the start and the destination.
     */
    public int distanceBetweenBusStops(int[] distance, int start, int destination) {
        int n = distance.length;
        int total = 0;
        int min = Integer.MAX_VALUE;

        // Calculate the total distance.
        for (int i = 1; i < n; i++) {
            total += distance[i];
            min = Math.min(min, distance[i]);
        }
        total += distance[0];
        total = Math.min(total, total - (distance[destination % n] + total - distance[start % n]));

        return Math.min(total, total - min);
    }

    public static void main(String[] args) {
        DistanceBetweenBusStops dbbs = new DistanceBetweenBusStops();
        int[] distance = {1, 2, 3, 4};
        int start = 0;
        int destination = 1;
        System.out.println(dbbs.distanceBetweenBusStops(distance, start, destination));
    }
}