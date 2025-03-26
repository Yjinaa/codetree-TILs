m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
months = [0,31,28,31,30,31,30,31,31,30,31,30,31]

# elapsed_time = (m2 * months[m2] + d2) - (m1 * months[m1] + d1)

elapsed_time = (sum(months[1:m2]) + d2) - (sum(months[1:m1]) + d1)
# sum(months[1:m2+1]) 해버리면 안됨 => 9월 8일이면 8월까지의 날을 전부 더하고 d2를 해야지 9월까지 더해버리면 9월 30일이 되는 셈
day = (0+elapsed_time) % 7

days = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}

print(days[day])