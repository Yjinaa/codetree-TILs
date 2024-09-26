n1 = int(input())
s1 = list(map(int, input().split()))

n2 = int(input())
s2 = list(map(int, input().split()))

s1 = set(s1)

for elem in s2:
    if elem in s1:
        print(1, end=" ")
    else:
        print(0, end=" ")