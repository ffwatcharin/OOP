day_month = [0, 31, 28,  31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    return ((year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0))

def day_of_year(day, month, year):
    day_of_years = 0
    if is_leap(year):
        day_month[2] += 1
    else:
        if month == 2 and day == 29:
            return -1
    for i in range(1, month):
        day_of_years += day_month[i]
    day_of_years += day

    return day_of_years

