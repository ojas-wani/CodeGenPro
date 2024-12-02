from datetime import datetime

class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = map(int, date.split('-'))
        return datetime(year, month, day).timetuple().tm_yday