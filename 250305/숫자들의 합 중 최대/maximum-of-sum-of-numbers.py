X, Y = map(int, input().split())

# Please write your code here.
# 자리수를 어떻게 하지..?

# score = 0
# for i in range(X,Y+1):
#     num = list(map(int, str(i)))
#     for j in range(len(num)):
#         score += (num[j]%10**(len(num)-j))//10**len(num)
# 아 걍 리스트라 sum하면 되네;;

# 탐색 범위: X ~ Y 까지의 수
ans = 0
for num in range(X, Y+1):
    # 각 자리 수의 합
    s = sum(list(map(int, list(str(num)))))
    
    ans = max(ans,s)

print(ans)