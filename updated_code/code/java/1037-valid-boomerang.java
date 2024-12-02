package com.example;

import java.util.Arrays;

/**
 * This class contains a method to check if three given points are a boomerang.
 */
public class BoomerangChecker {
    /**
     * This method checks if three points are a boomerang.
     * 
     * @param points An array of three points, where each point is an array of two integers.
     * @return True if the points are a boomerang, false otherwise.
     */
    public boolean isBoomerang(int[][] points) {
        if (points.length != 3) {
            throw new IllegalArgumentException("Input array should have exactly 3 points.");
        }

        // Check if all points are distinct
        if (!Arrays.stream(points).distinct().count() == 3) {
            return false;
        }

        // Calculate the slopes of the lines formed by the points
        double slope12 = (points[1][1] - points[0][1]) * 1.0 / (points[1][0] - points[0][0]);
        double slope23 = (points[2][1] - points[1][1]) * 1.0 / (points[2][0] - points[1][0]);
        double slope31 = (points[0][1] - points[2][1]) * 1.0 / (points[0][0] - points[2][0]);

        // Check if the points are not in a straight line
        if (slope12 == slope23 || slope23 == slope31 || slope31 == slope12) {
            return false;
        }

        return true;
    }
}