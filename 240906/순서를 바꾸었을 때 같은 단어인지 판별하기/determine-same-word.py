from collections import Counter

a = input()
b = input()

ac = Counter(a)
bc = Counter(b)

print('Yes' if ac == bc else 'No')