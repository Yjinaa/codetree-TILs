class Student:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math


n = int(input())

students = []
for i in range(n):
    name, k, e, m = input().split()
    k, e, m = int(k), int(e), int(m)
    students.append(Student(name, k, e, m))
    
students.sort(lambda x:(-x.kor, -x.eng, -x.math))

for i in range(n):
    print(students[i].name, students[i].kor, students[i].eng, students[i].math)