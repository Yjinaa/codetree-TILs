class LetsMeet:
    def __init__(self, code, location, time):
        self.code = code
        self.location = location
        self.time = time

    # def show(self):
    #     print(f'secret code: {self.code}')
    #     print(f'meeting point: {self.location}')
    #     print(f'time: {self.time}')

scode, slocation, stime = map(str, input().split())
stime = int(stime)

meet = LetsMeet(scode, slocation, stime)

print(f'secret code : {meet.code}')
print(f'meeting point : {meet.location}')
print(f'time : {meet.time}')