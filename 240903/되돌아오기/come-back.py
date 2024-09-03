def find_answer(n):
    x, y = 0,0
    t = 0

    for i in range(n):
        direction, distance = input().split()
        d = dir_map[direction]
        distance = int(distance)

        for j in range(distance):
            nx, ny = x + dx[d], y + dy[d]
            x, y = nx, ny
            t += 1

            if nx == 0 and ny == 0:
                return (t)
    return -1

n = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

dir_map = {'E':0, 'W':1, 'S':2, 'N':3}

print(find_answer(n))