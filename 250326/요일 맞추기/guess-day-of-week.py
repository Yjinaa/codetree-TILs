m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
months = [0,31,28,31,30,31,30,31,31,30,31,30,31]

elapsed_time = (m2 * months[m2] + d2) - (m1 * months[m1] + d1)

day = (0+elapsed_time) % 7

days = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}

print(days[day])