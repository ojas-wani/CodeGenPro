class Solution:
    def reformatDate(self, date: str) -> str:
        months = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
        day = date.split()[-1].replace("st", "").replace("nd", "").replace("rd", "")
        month = months[date.split()[1]]
        year = date.split()[2]
        return f"{year}-{month}-{day}"