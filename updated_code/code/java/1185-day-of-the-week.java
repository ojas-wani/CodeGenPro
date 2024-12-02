package com.example;

import java.time.LocalDate;
import java.time.DayOfWeek;

/**
 * This class determines the day of the week for a given date.
 */
public class Solution {

    /**
     * This method calculates and returns the day of the week for a given date.
     * 
     * @param day   the day of the month (1-31)
     * @param month the month of the year (1-12)
     * @param year  the year (1971-2100)
     * @return the day of the week as a string ("Sunday", "Monday", etc.)
     */
    public String dayOfTheWeek(int day, int month, int year) {
        final LocalDate date = LocalDate.of(year, month, day);
        final DayOfWeek dayOfWeek = date.getDayOfWeek();
        final String[] daysOfWeek = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};
        return daysOfWeek[dayOfWeek.ordinal()];
    }
}