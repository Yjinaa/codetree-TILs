k, n = map(int, input().split())

arr = []

def get_numpairs(cur_num):
    if cur_num == n+1:
        print(*arr)
        return
    
    for i in range(1,k+1):
        arr.append(i)
        get_numpairs(cur_num+1)
        arr.pop()

    return

get_numpairs(1)