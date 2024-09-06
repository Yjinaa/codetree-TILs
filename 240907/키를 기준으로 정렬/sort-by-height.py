class User:
    def __init__(self,name,height,weight):
        self.name = name
        self.height = height
        self.weight = weight


n = int(input())

users = []
for i in range(n):
    name, h, w = input().split()
    users.append(User(name, h, w))

users.sort(key=lambda x:x.height)

for i in range(n):
    print(f'{users[i].name} {users[i].height} {users[i].weight}')