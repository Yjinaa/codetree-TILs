n = int(input())

for i in range(n):
    for j in range(n-i): # 패착:range(n)하면 0부터 시작하니까 n을 걍 0이라고 생각함..ㅠ
        print('*'*(n-i), end=" ") # 그리고 j는 역할이 없다. 걍 반복횟수를 담당하는 변수임
    print()


