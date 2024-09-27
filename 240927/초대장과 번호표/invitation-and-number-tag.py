n, g = map(int, input().split())

groups = sorted([list(map(int, input().split())) for _ in range(g)], key=lambda x:x[0])

invited = {1}

for group in groups:
    group.pop(0)
    remaining_list = [x for x in group if x not in invited]
    if len(remaining_list) == 1:
        invited.update(remaining_list)

print(len(invited))