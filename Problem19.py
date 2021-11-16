def isLeap(year):
    ans = False
    if year%4 == 0:
        ans = True
    if year%100 == 0:
        ans = False
    if year%400 == 0:
        ans = True
    return ans

day = 1
month = 1
year = 1900
weekday = 1
monthSize = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
total = 0
while True:
    if year > 2000:
        break
    if year >= 1901 and year <= 2000 and day == 1 and weekday%7 == 0:
        total += 1
    weekday += 1
    day += 1
    if day > monthSize[month]:
        day = 1
        month += 1
    if month > 12:
        month = 1
        day = 1
        year += 1
        if isLeap(year):
            monthSize[2] = 29
        else:
            monthSize[2] = 28
print(total)