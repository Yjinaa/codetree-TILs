n = int(input())
numbers = list(map(int, input().split()))

# Please write your code here.

max_sum = 0
cur_sum = 0
for i in range(n-2):
    for j in range(i+1, n):
        cur_sum = max(cur_sum, numbers[i]+numbers[j])
    max_sum = max(cur_sum, max_sum)

print(max_sum)