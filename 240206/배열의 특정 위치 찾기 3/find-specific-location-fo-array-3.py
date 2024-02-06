nums = list(map(int, input().split()))
new = []
for elem in nums:
    if elem != 0:
        new.append(elem)
    else:
        break

print(sum(new[-3::1]))