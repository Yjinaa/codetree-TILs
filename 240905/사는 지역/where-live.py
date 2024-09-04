class Person:
    def __init__(self, name, code, location):
        self.name = name
        self.code = code
        self.location = location

n = int(input())

people = []

for i in range(n):
    name, code, location = input().split()
    people.append(Person(name, code, location))

target_idx = 0
for i, person in enumerate(people):
    if person.name > people[target_idx].name:
        target_idx = i 

print(f'name {people[target_idx].name}')
print(f'name {people[target_idx].code}')
print(f'name {people[target_idx].location}')