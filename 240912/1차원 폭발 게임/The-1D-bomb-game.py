from collections import defaultdict
n,m = map(int, input().split())

b = [int(input()) for _ in range(n)]

end = False
def bombs(b,m,end):
    end = False
    d = defaultdict(int)
    for i in range(len(b)-1):
        if b[i] == b[i+1]:
            d[b[i]] += 1
    if len(d) == 0:
        end = True
        return end, after_bomb
    for key in d.keys():
        if d[key] + 1 >= m:
            after_bomb = remove(b, key)
    return end, after_bomb

def remove(b, key):
    temp = []
    for i in range(len(b)):
        if b[i] != key:
            temp.append(b[i])
    return temp

while True:
    if len(b) > 0:
        end, b = bombs(b,m,end)
    else:
        break
    if end == True:
        break

if len(b) == 0:
    print(0)
else:
    print(len(b))
    for bomb in b:
        print(bomb)