m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.

months = [0,31,29,31,30,31,30,31,31,30,31,30,31]

diff = (sum(months[1:m2])+d2) - (sum(months[1:m1])+d1)

day = diff // 7

days = {'Mon':0,'Tue':1,'Wed':2,'Thu':3,'Fri':4,'Sat':5,'Sun':6}

if diff % 7 >= days[A]:
    print(day+1)
else:
    print(day)