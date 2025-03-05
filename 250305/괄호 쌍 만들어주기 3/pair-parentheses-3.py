A = list(input())

# n이 10000이하면 n^3 안됨 100까진 가능
# Please write your code here.

cnt = 0

for i in range(len(A)):
    if A[i] == '(':
        for j in range(i+1,len(A)): # i번째 문자부터 끝까지 비교
            if A[j] == ')':
                cnt += 1

print(cnt)

# 모든 위치 쌍
# for i in range(len(A)):
#     for j in range(i+1,len(A)):
#         if A[i] == '(' and A[j] == ')':
#             cnt += 1