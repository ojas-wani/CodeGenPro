class Solution {
    public int dayOfYear(String date) {
        String[] yearMonthDay = date.split (“-”);
        int year = Integer.parseInt(yearMonthDay[0]);
        int month = Integer.parseInt(yearMonthDay[1]);
        int day = Integer.parseInt(yearMonthDay[2]);
        
        int[] daysInMonth = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        
        if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) {
            daysInMonth[1] = 29;
        }
        
        int totalDays = 0;
        
        for (int i = 0; i < month - 1; i++) {
            totalDays += daysInMonth[i];
        }
        
        return totalDays + day;
    }
}