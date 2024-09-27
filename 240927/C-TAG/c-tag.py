# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))
A = [input() for _ in range(n)]
B = [input() for _ in range(n)]

ans = 0
s = set()

def test_location(x, y, z):
    # x, y, z번째 자릿수를 선택했을 때 A와 B 그룹이
    # 완벽하게 구분되면 true, 그렇지 않다면 false를 반환합니다.
    s.clear()

    # A의 원소를 전부 HashSet에 넣어줍니다.
    for i in range(n):
        s.add(A[i][x] + A[i][y] + A[i][z])
    
    # B의 원소 중 하나라도 A와 같은 경우가 있다면
    # A와 B를 구분해낼 수 없습니다.
    for i in range(n):
        if (B[i][x] + B[i][y] + B[i][z]) in s:
            return False
    
    # 모든 B의 원소가 A와 다르다면 A와 B를 구분해낼 수 있습니다.
    return True

# 서로 다른 세 자리의 조합을 모두 순회합니다.
for i in range(m):
    for j in range(i + 1, m):
        for k in range(j + 1, m):
            # i, j, k 번째 자리를 선택했을 때 두 그룹을
            # 완벽하게 구분할 수 있는지 확인합니다.
            if test_location(i, j, k): ans += 1

# 두 그룹을 구분해낼 수 있는 조합 수를 출력합니다.
print(ans)