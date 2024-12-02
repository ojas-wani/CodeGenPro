import java.time.LocalDate;
import java.time.Year;
import java.time.format.DateTimeFormatter;
import java.time.temporal.ChronoUnit;

public class Solution {
    public int dayOfYear(String date) {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd");
        LocalDate localDate = LocalDate.parse(date, formatter);
        return (int) ChronoUnit.DAYS.between(LocalDate.ofYearDay(Year.now().getValue(), 1), localDate);
    }
}