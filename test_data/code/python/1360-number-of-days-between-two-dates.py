Python
from datetime import datetime

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        dt1 = datetime.strptime(date1, '%Y-%m-%d')
        dt2 = datetime.strptime(date2, '%Y-%m-%d')
        
        return abs((dt2 - dt1).days)