/**
 * Solution class
 * Count the number of days between two dates.
 * The two dates are given as strings, their format is YYYY-MM-DD.
 */
package solution;

import java.time.LocalDate;
import java.time.temporal.ChronoUnit;

public class Solution {
    /**
     * Count the number of days between two dates.
     * @param date1 the start date
     * @param date2 the end date
     * @return the number of days between date1 and date2
     */
    public int daysBetweenDates(String date1, String date2) {
        LocalDate localDate1 = LocalDate.parse(date1);
        LocalDate localDate2 = LocalDate.parse(date2);
        final long days = ChronoUnit.DAYS.between(localDate1, localDate2);
        return (int) days;
    }
}