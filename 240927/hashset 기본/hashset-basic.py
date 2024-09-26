s = set()
def find(num):
    if num in s:
        return "true"
    else:
        return "false"

def add(num):
    s.add(num)

def remove(num):
    s.remove(num)

n = int(input())

for i in range(n):
    command, num = input().split()
    num = int(num)
    if command == 'find':
        print(find(num))
    elif command == 'add':
        add(num)
    else:
        remove(num)