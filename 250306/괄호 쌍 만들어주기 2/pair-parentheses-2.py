A = input()

# Please write your code here.

# cnt = 0
# for i in range(len(A)-1):
#     if A[i] == '(' and A[i+1] == '(':
#         for j in range(i+2, len(A)-1):
#             if A[j] == ')' and A[j+1] == ')':
#                 cnt += 1

# print(cnt)

# ===================
# 리스트 슬라이싱 사용
# ===================

cnt = 0
for i in range(len(A)-1):
    if A[i:i+2] == '((':
        for j in range(i+2, len(A)-1):
            if A[j:j+2] == '))':
                cnt += 1
print(cnt)