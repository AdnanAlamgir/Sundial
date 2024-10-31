
def gen_days(day, month, year):

    if year % 100 != 0 and year % 4 == 0:
        mon_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    elif year % 100 == 0 and year % 400 == 0:
        mon_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        mon_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    days = 0
    for i in range(month - 1):
        days += mon_days[i]
    days += day

    return days

print(gen_days(31, 3, 2024))
