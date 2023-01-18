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


def day_in_year(year):
    if is_leap(year):
        return 366
    else:
        return 365


def date_diff(date1, date2):
    data1 = [int(i) for i in date1.split('-')]
    data2 = [int(i) for i in date2.split('-')]

    sum_data1 = day_of_year(data1[0], data1[1], data1[2])
    sum_data2 = day_of_year(data2[0], data2[1], data2[2])
    day_between = 0

    for year in range(data1[2], data2[2]):
        day_between += day_in_year(year)

    if (data1[1] > 12 or data1[1] < 1 or data2[1] > 12 or data2[1] < 1):
        return -1
    elif (data1[0] == 29 and data1[1] == 2 and not is_leap(data1[2])) or (data2[0] == 29 and data2[1] == 2 and not is_leap(data2[2])):
        return -1
    elif (data1[0] > day_month[data1[1]] or data1[0] < 0) or (data2[0] > day_month[data2[1]] or data2[0] < 0):
        return -1
    else:
        return day_between - sum_data1 + sum_data2 + 1
