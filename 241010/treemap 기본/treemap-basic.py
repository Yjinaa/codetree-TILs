from sortedcontainers import SortedDict

n = int(input())
sd = SortedDict()

for i in range(n):
    command = list(input().split())

    if command[0] == 'add':
        sd[int(command[1])] = int(command[2])
    elif command[0] == 'remove':
        sd.pop(int(command[1]))
    elif command[0] == 'find':
        if int(command[1]) in sd:
            print(sd[int(command[1])])
        else:
            print(None)
    elif command[0] == 'print_list':
        if sd:
            for value in sd.values():
                print(value, end=" ")
            print()
        else:
            print(None)