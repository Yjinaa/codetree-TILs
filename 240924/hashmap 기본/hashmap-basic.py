n = int(input())
d = {}

def add(k,v):
    d[k] = v

def remove(k):
    d.pop(k)

def find(k):
    if k in d:
        print(d[k])
    else:
        print(None)

for i in range(n):
    command = list(input().split())
    if command[0] == 'add':
        add(int(command[1]),int(command[2]))
    elif command[0] == 'remove':
        remove(int(command[1]))
    else:
        find(int(command[1]))