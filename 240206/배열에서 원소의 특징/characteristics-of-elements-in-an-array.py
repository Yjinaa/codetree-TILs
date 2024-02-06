nums = list(map(int, input().split()))
new = []
for elem in nums:
    if elem % 3 != 0:
        new.append(elem)
    else:
        break

print(new[-1])