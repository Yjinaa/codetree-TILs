n = int(input())
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

# Please write your code here.

blocks[-s1:-e1-1:-1] = [0]*(e1-s1+1)
temp = []
for i in range(len(blocks)):
    if blocks[i] != 0:
        temp.append(blocks[i])
blocks = temp

blocks[-s2:-e2-1:-1] = [0]*(e2-s2+1)
temp = []
for i in range(len(blocks)):
    if blocks[i] != 0:
        temp.append(blocks[i])

print(len(temp))
for k in temp:
    print(k)