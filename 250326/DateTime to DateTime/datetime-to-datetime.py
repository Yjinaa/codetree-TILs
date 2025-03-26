a, b, c = map(int, input().split())

# Please write your code here.

months = [0,31,28,31,30,31,30,31,31,30,31,30,31]

month = 11
day = 11
hour = 11
mins = 11
elapsed_time = 0

while True:
    if day == a and hour == b and mins == c:
        print(elapsed_time)
        break
    mins += 1
    elapsed_time += 1
    if mins == 60:
        hour += 1
        mins = 0
        if hour == 24:
            day += 1
            hour = 0

