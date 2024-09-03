# 레이저가 '출발한' 방향이 아니고 레이저 '자체'의 방향
# 즉, 1,2,3은 남쪽방향 레이저(북쪽 아님), 4,5,6은 서쪽방향 레이저(동쪽 아님)
n = int(input())
mirrors = []
for _ in range(n):
    row = list(input())
    mirrors.append(row)
k = int(input())
dir_map = {'E':0, 'S':1, 'W':2, 'N':3}

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

if 1 <= k <= n:
    laser = 'S'
    x, y = 0, k-1
elif n+1 <= k <= 2*n:
    laser = 'W'
    x, y = k-n-1, n-1
elif 2*n+1 <= k <= 3*n:
    laser = 'N'
    x, y = n-1, 3*n-k
else:
    laser = 'E'
    x, y = 4*n-k, 0

def find_answer(x,y,laser):
    cnt = 0
    while True:
        if mirrors[x][y] == '\\':
            if laser == 'N':
                d = dir_map['W']
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < n and 0 <= ny < n:
                    cnt += 1
                    x, y = nx, ny
                    laser = 'W'
                else:
                    return cnt + 1      
            if laser == 'E':
                d = dir_map['S']
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < n and 0 <= ny < n:
                    cnt += 1
                    x, y = nx, ny
                    laser = 'S'                    
                else:                
                    return cnt + 1      
            if laser == 'S':
                d = dir_map['E']
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < n and 0 <= ny < n:
                    cnt += 1
                    x, y = nx, ny 
                    laser = 'E'                   
                else:                
                    return cnt + 1                          
            if laser == 'W':
                d = dir_map['N']
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < n and 0 <= ny < n:
                    cnt += 1
                    x, y = nx, ny 
                    laser = 'N'                   
                else:                
                    return cnt + 1      
        elif mirrors[x][y] == '/':
            if laser == 'N':
                d = dir_map['E']
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < n and 0 <= ny < n:
                    cnt += 1
                    x, y = nx, ny    
                    laser = 'E'                
                else:                
                    return cnt + 1      
            if laser == 'E':
                d = dir_map['N']
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < n and 0 <= ny < n:
                    cnt += 1
                    x, y = nx, ny     
                    laser = 'N'               
                else:                
                    return cnt + 1      
            if laser == 'W':
                d = dir_map['S']
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < n and 0 <= ny < n:
                    cnt += 1
                    x, y = nx, ny    
                    laser = 'S'                
                else:                
                    return cnt + 1      
            if laser == 'S':
                d = dir_map['W']
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < n and 0 <= ny < n:
                    cnt += 1
                    x, y = nx, ny       
                    laser = 'W'             
                else:                
                    return cnt + 1                                                                        

print(find_answer(x,y,laser))