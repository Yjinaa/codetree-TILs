times = list(map(int, input().split()))

m1, d1, m2, d2 = times


days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

start = 0
end = 0

for i in range(m1):
    start += days[i]
start += d1

for i in range(m2):
    end += days[i]
end += d2

print(end - start +1)