n, g = map(int, input().split())

groups = sorted([list(map(int, input().split())) for _ in range(g)], key=lambda x:x[0])
groups = [group[1:] for group in groups]
invited = {1}

while True:
    is_changed = False
    for group in groups:
        if len(set(group) - invited) == 1:
            invited.update(set(group)-invited)
            is_changed = True
    if is_changed == False:
        break

print(len(invited))