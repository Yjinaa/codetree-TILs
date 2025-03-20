n = int(input())
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

# Please write your code here.

s = [s1,s2]
e = [e1,e2]

for t in range(2):
    blocks[s[t]-1:e[t]] = [0]*(e[t]-s[t]+1)
    temp = []
    for i in range(len(blocks)):
        if blocks[i] != 0:
            temp.append(blocks[i])
    blocks = temp

print(len(temp))
for k in temp:
    print(k)