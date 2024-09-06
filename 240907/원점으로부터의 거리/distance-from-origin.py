class Points:
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.num = num


n = int(input())

ps = []
for i in range(n):
    x, y = map(int, input().split())
    ps.append(Points(x,y,i+1))

def manhattan_distance(p1, p2):
    return abs(p1.x-p2.x) + abs(p1.y-p2.y)

ps.sort(key=lambda x:manhattan_distance(Points(0,0,0), x))

for i in range(n):
    print(ps[i].num)