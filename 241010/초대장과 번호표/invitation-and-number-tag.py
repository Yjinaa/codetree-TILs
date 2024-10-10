n, g = map(int, input().split())

invited = set({1})

for i in range(g):
    p = set((list(map(int, input().split())))[1:])
    if len(p-invited) == 1:
        invited.update(p-invited)

print(len(invited))