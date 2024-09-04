class Bomb:
    def __init__(self, code, color, time):
        self.code = code
        self.color = color
        self.time = time

code, c, t = input().split()
sol = Bomb(code, c, t)

print(f'code : {sol.code}')
print(f'color : {sol.color}')
print(f'second : {sol.time}')