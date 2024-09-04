class Data:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

n = int(input())

datas = []

for i in range(n):
    date, day, weather = input().split()
    if weather == 'Rain':
        datas.append(Data(date, day, weather))

min_date = '9999-99-99'
for i in range(len(datas)):
    if datas[i].date < min_date:
        min_date = datas[i].date
        min_idx = i

print(datas[min_idx].date, datas[min_idx].day, datas[min_idx].weather)