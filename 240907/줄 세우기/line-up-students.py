n = int(input())

class Student:
    def __init__(self, h, w, num):
        self.height = h 
        self.weight = w 
        self.num = num

students = []
for i in range(n):
    h, w = map(int, input().split())
    students.append(Student(h, w, i+1))

students.sort(lambda x: (-x.height, -x.weight, x.num))

for i in range(n):
    print(students[i].height, students[i].weight, students[i].num)