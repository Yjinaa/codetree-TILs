n, g = map(int, input().split())

invited = set({1})
invitation = []

for i in range(g):
    p = list(map(int, input().split()))[1:]
    invitation.append(p)

while True:
    is_updated = False
    for p in invitation:
        p = set(p)
        if len(p-invited) == 1:
            invited.update(p-invited)
            is_updated = True
    if is_updated == False:
        break

print(len(invited))