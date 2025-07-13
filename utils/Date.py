import datetime as dt


class Date(dt.date):
    def __new__(cls, year: int, month: int, dayy: int):
        return super().__new__(cls, year, month, dayy)

    def __add__(self, days: int) -> "Date":
        new_date = super().__add__(dt.timedelta(days=days))
        return Date(new_date.year, new_date.month, new_date.day)

    def __sub__(self, days: int) -> "Date":
        new_date = super().__sub__(dt.timedelta(days=days))
        return Date(new_date.year, new_date.month, new_date.day)

    @staticmethod
    def get_days_in_month(year: int, month: int) -> int:
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif month in [4, 6, 9, 11]:
            return 30
        elif month == 2:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                return 29
            else:
                return 28
        else:
            raise ValueError("Invalid month")

    @staticmethod
    def get_weekday_name(weekday: int) -> str:
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        return days[weekday]

    @staticmethod
    def get_month_name(month: int) -> str:
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        return months[month - 1]

    @staticmethod
    def get_future_month_name(month: int) -> str:
        months = ["F", "G", "H", "J", "K", "M", "N", "Q", "U", "V", "X", "Z"]
        return months[month - 1]

    @staticmethod
    def Today() -> "Date":
        today = dt.date.today()
        return Date(today.year, today.month, today.day)

    def get_day_of_week(self) -> str:
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        return days[self.weekday()]

    def is_IMM(self) -> bool:
        return self.get_day_of_week() == "Wed" and self.day > 14 and self.day <= 21 and self.month in [3, 6, 9, 12]
