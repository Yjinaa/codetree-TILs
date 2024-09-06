class Student:
    def __init__(self, name, a, b, c):
        self.name = name
        self.a = a
        self.b = b
        self.c = c 


n = int(input())

students = []

for i in range(n):
    name, a, b, c = input().split()
    a, b, c = int(a), int(b), int(c)

    students.append(Student(name, a, b, c))

students.sort(key=lambda x:x.a + x.b + x.c)

for i in range(n):
    print(students[i].name, students[i].a, students[i].b, students[i].c)