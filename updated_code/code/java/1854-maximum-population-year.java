package org.example;

import java.util.Arrays;

public class MaximumPopulationYear {
    public int maximumPopulation(int[][] logs) {
        int[] count = new int[101]; // Initialize array with 101 elements
        // Consider using varargs for methods or constructors which take an array the last parameter.
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

    public static void main(String[] args) {
        MaximumPopulationYear solution = new MaximumPopulationYear();
        int[][] logs = {{1993,1999},{2000,2010}};
        int result = solution.maximumPopulation(logs);
        System.out.println("The maximum population year is: " + result);
    }
}