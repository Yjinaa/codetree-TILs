# 11월 11일 0시 0분 기준

times = list(map(int, input().split()))

a,b,c = times

if a == 11 and b < 11:
    print (-1)
elif a < 11:
    print(-1)
elif a == 11 and b == 11 and c < 11:
    print(-1)
else:
    days = a-11

    start = 60 * 11 + 11
    end = b * 60 + c

    mins = end - start + (days * 24 * 60)

    print(mins)