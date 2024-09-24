from collections import Counter

s = input()
c = Counter(s)

found = False
for key in c:
    if c[key] == 1:
        print(key)
        found = True
        break

if found == False:
    print(None)