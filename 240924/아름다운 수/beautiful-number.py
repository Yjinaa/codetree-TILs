n = int(input())

arr = []
cnt = 0

def is_beautiful(arr):
    if len(arr) == 1:
        if arr[0] == 1:
            return True
        else:
            return False
    start_idx = 0
    for end_idx in range(1,len(arr)):
        print(end_idx)
        if arr[end_idx] != arr[start_idx]:
            if arr[end_idx-1] != len(arr[start_idx:end_idx]):
                return False
            start_idx = end_idx
        elif end_idx == len(arr)-1:
            if len(arr[start_idx:end_idx]) % arr[end_idx-1] != 0:
                return False      
    return True


def get_beautiful_number(cur_num):
    global cnt
    if cur_num == n+1:
        if is_beautiful(arr) == True:
            cnt += 1
        return
    
    for i in range(1,5):
        arr.append(i)
        get_beautiful_number(cur_num+1)
        arr.pop()
    return

get_beautiful_number(n)
print(cnt)