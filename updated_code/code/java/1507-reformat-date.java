package com.example.solution;

import java.util.Arrays;

/**
 * Solution to reformat date format
 */
public class Solution {
    public String reformatDate(String date) {
        String[] parts = date.split(" ");
        int day = Integer.parseInt(parts[0].replace("st", "").replace("nd", "").replace("rd", "").replace("th", ""));
        String month = parts[1];
        int year = Integer.parseInt(parts[2]);

        String[] months = {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"};

        int monthIndex = -1;
        for (int i = 0; i < months.length; i++) {
            if (months[i].equals(month)) {
                monthIndex = i + 1;
                break;
            }
        }

        return String.format("%04d-%02d-%02d", year, monthIndex, day);
    }
}