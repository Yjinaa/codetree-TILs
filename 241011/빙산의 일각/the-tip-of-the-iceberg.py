# n 입력
n = int(input())
# ice_berg
ice_berg = list()
# h(i) 입력
for _ in range(n):
    ice_berg.append(int(input()))

# 함수들
# simulate(curr_height)
def simulate(curr_height):
    
    # curr_cnt
    curr_cnt = 0

    # 맨 왼쪽은 떠있으면
    if ice_berg[0] > curr_height:
        # curr_cnt에 추가
        curr_cnt += 1

    # 이후의 ice_berg를 돌면서
    for i in range(1, n):
        # 전 인덱스가 잠겼고, 자기는 떠있으면
        if ice_berg[i-1] <= curr_height and ice_berg[i] > curr_height:
            # curr_cnt에 추가
            curr_cnt += 1    

    # curr_cnt 반환
    return curr_cnt

# 설계
# max_cnt
max_cnt = 0

# max_height
max_height = max(ice_berg)

# 완전 탐색 시작
for i in range(max_height):
    # max_cnt 업데이트
    max_cnt = max(max_cnt, simulate(i))

# 출력
print(max_cnt)