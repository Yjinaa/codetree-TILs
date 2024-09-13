n = int(input())
x, y = map(int, input().split())
x, y = x-1, y-1

grid = [list(input()) for _ in range(n)]
visited = set()

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

d = 0

# 오른쪽에 벽이 있는지 확인하는 함수
def is_wall(d, x, y):
    d = (d+1)%4
    nx, ny = x + dx[d], y+dy[d]
    # print('wall?',nx, ny)
    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == '#':
        # print('wall')
        return True
    else:
        # print('no wall')
        return False

# 앞으로 이동 가능한지 확인하는 함수
def go_avilable(d, x, y):
    nx, ny = x+dx[d], y+dy[d]
    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == '.':
        # print('True')
        return True
    elif not(0 <= nx < n and 0 <= ny < n):
        # print('OOG')
        return 'OOG Available'
    else:
        # print('False')
        return False

def move_available(x, y):
    for i in range(4):
        nx, ny = x +dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == '.':
            return True
    return False

def simulate(d, x, y):
    t = 0
    while True:
        if move_available(x,y)==False:
            return -1
        visited.add((d, x, y))
        if is_wall(d, x, y): # 오른쪽에 벽이 있을 때
            available = go_avilable(d, x, y)
            if not available: # 바라보고 있는 방향, 이동 불가능 할 때
                d = (d+3)%4
                # print(x,y,d)
            elif available == 'OOG Available': # 바라보고 있는 방향, 탈출 가능 할 때
                # print('OOG available')
                break
            elif available==True: # 바라보고 있는 방향, 이동 가능 할 때
                nx, ny = x+dx[d], y+dy[d]
                if (d, x, y) not in visited:
                    x, y = nx, ny
                    t += 1
                else:
                    return -1
        else: # 오른쪽에 벽이 없을 때
            d = (d+1)%4
            nx, ny = x+dx[d], y+dy[d]
            x, y = nx, ny
            t += 1
            # print(x,y,d,'else')
    return t+1

t = simulate(d, x, y)
print(t)