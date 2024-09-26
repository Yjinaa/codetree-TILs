from collections import defaultdict
n,k = map(int, input().split())

s = defaultdict(int)
seats = defaultdict(set)

for i in range(n):
    s[i+1] = i+1
    seats[i+1].add(i+1)

seat_list = []
for i in range(k):
    p1, p2 = map(int, input().split())
    seat_list.append((p1,p2))

for i in range(3):
    for p1, p2 in seat_list:
        seats[s[p1]].add(p2)
        seats[s[p2]].add(p1)
        s[p1], s[p2] = s[p2], s[p1]

for person in seats.keys():
    print(len(seats[person]))