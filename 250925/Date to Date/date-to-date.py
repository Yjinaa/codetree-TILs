m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
months = [0,31,28,31,30,31,30,31,31,30,31,30,31]

print(sum(months[:m2]) + d2 - (sum(months[:m1]) + d1) + 1)