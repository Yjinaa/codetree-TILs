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


# =====================
# 자리수가 유동적일 경우
# =====================

# def sum_of_digits(num):
#     result = 0
    
#     # ========================================
#     # 1의 자리부터 떼면서 num을 한자리씩 소거
#     # ========================================
#     while num > 0: 
#         result += num % 10
#         num /= 10

#     # ========================================
#     # 최대 범위부터 num을 한자리씩 소거
#     # ========================================
#     for i in range(1,10000,i*10):
#         result += (num/i*10) % i

#     result += (num / 10000) % 1000
#     result += (num / 1000) % 100
#     result += (num / 100) % 10
#     result += (num / 10) % 1
    
#     return result

# ans = 0
# for num in range(X, Y+1):
#     result = sum_of_digits(num)
#     ans = max(ans, result)