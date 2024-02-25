def get_day_of_week(input_date):
    day_of_week = input_date.weekday()
    days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
    return days[day_of_week]