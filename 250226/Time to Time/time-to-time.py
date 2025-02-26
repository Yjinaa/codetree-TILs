a, b, c, d = map(int, input().split())

# Please write your code here.
hours = c-a

if b > d:
    hours -= 1
    minutes = 60-b + d
elif b == d:
    minutes = 0
else:
    minutes = d - b

print(60*hours + minutes)