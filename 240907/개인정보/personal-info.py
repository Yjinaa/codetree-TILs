class Person:
    def __init__(self, name, h, w):
        self.name = name
        self.height = h 
        self.weight = w 

people = []

for i in range(5):
    name, h, w = input().split()
    people.append(Person(name, int(h), round(float(w),1)))

print('name')
ns = sorted(people, key=lambda x:x.name)
for i in range(5):
    print(ns[i].name, ns[i].height, ns[i].weight)
print()
print('height')
hs = sorted(people, key=lambda x:-x.height)
for i in range(5):
    print(hs[i].name, hs[i].height, hs[i].weight)