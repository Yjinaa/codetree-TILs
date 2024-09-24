from collections import Counter

s = input()

c = Counter(s)

found = False
for key in c:
    if c[key] == 1:
        print(key)
        found = True

if found == False:
    print(None)