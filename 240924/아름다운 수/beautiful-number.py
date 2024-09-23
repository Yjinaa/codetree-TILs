n = int(input())

arr = []
cnt = 0

def is_beautiful(arr):
    # print(arr)
    if len(arr) == 1:
        if arr[0] == 1:
            return True
        else:
            return False
    start_idx = 0
    for end_idx in range(1,len(arr)):
        if arr[end_idx] != arr[start_idx]:
            if arr[end_idx-1] != end_idx-start_idx: 
                return False
            start_idx = end_idx
            # print(arr, start_idx)
    if start_idx == 0:
        if len(arr) % arr[start_idx] == 0:
            return True
    if len(arr) - start_idx != arr[start_idx]:
        return False
    # if len(arr) % arr[start_idx] != 0:
    #     return False
    # print(arr, True)
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

get_beautiful_number(1)
print(cnt)