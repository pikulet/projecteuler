# Problem 19

START_YEAR = 1900
END_YEAR = 2000

def is_leap_year(y):
    return y % 4 == 0 and not y % 100 == 0 or y % 400 == 0

def add_days(num_days):
    global CURRENT_DAY
    CURRENT_DAY = (CURRENT_DAY + num_days) % 7

DAYS = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

CURRENT_DAY = 1 # Monday, START_YEAR
add_days(365)
if is_leap_year(START_YEAR):
    add_days(1)

result = 0
for year in range(START_YEAR + 1, END_YEAR + 1):
    for month in range(1, 13):
        if CURRENT_DAY == 0:
            result += 1
        add_days(DAYS[month])
        if month == 2 and is_leap_year(year):
            add_days(1)

print(result)
