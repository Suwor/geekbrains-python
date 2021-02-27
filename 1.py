from datetime import datetime


class Date:
    @staticmethod
    def validate(date):
        day, month, year = date.split('-')
        return 0 < int(day) < 32 and 0 < int(month) < 13 and 1970 < int(year) < 3000

    @classmethod
    def get_unix_time(cls, date):
        if cls.validate(date):
            return datetime.strptime(date, "%d-%m-%Y").timestamp()
        else:
            return "Некорректный формат даты"

    def __init__(self, date):
        self.date = date


my_date = Date("11-10-2017")
print(Date.get_unix_time(my_date.date))
