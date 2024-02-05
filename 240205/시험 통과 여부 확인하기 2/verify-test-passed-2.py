n = int(input())

passes = 0
for _ in range(n):
    scores = list(map(int, input().split()))
    mean_s = sum(scores)/len(scores)
    if mean_s >= 60:
        passes += 1
        print('pass')
    else:
        print('fail')
        print(passes)