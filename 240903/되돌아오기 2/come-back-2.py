dirs = list(input())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def find_answer(dirs, d):
    t = 0
    x, y = 0, 0
    for direction in dirs:
        t += 1
        if direction == 'L':
            d = (d+3) % 4
        elif direction == 'R':
            d = (d+1) % 4
        else:
            nx, ny = x + dx[d], y + dy[d]
            x, y = nx, ny
            if nx == 0 and ny == 0:
                return t
    return -1

d = 3

print(find_answer(dirs, d))