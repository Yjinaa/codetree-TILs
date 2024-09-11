n = int(input())

b = [int(input()) for _ in range(n)]

s1, e1 = map(int, input().split())
s1, e1 = s1-1, e1-1
s2, e2 = map(int, input().split())
s2, e2 = s2-1, e2-1

temp = []

def remove_block(s,e,b):
    temp = []
    for i in range(len(b)):
        if i >= s and i <= e:
            continue
        else:
            temp.append(b[i])
    return temp

for i in range(2):
    b1 = remove_block(s1, e1, b)
    fin = remove_block(s2, e2, b1)

print(len(fin))
for block in fin:
    print(block)