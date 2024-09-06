class Student:
    def __init__(self, h, w, num):
        self.h = h
        self.w = w
        self.num = num

N = int(input())

students = []
for i in range(N):
    h, w = map(int, input().split())
    students.append(Student(h, w, i+1))

students.sort(lambda x: (x.h, -x.w))

for i in range(N):
    print(students[i].h, students[i].w, students[i].num)