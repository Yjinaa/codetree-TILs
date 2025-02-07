n = int(input())

def is_one(n):
    cnt = 0
    if n == 1:
        return cnt
    while True:
        if n % 2 == 0:
            n = n/2
        else:
            n = n*3+1
        
        if n == 1:
            cnt += 1
            break
        else:
            cnt += 1

    return cnt

print(is_one(n))