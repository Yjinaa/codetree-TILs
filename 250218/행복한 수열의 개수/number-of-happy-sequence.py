n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Write your code here!

# def get_happies(grid):
#     happies = 0
#     for i in range(2):
#         for row in range(n):
#             nums = []
#             for col in range(n):
#                 nums.append(grid[row][col])
#             cnt = Counter(nums)
#             if m in cnt.values():
#                 happies += 1
#         grid = list(map(list, zip(*grid)))
#     return happies


# print(get_happies(grid))
# 작업이 복잡할 땐 작은 작업 단위로 나눠보기
def check_happy(nums, m):
    cnt, max_cnt = 1, 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            cnt += 1
        else:
            cnt = 1
        max_cnt = max(max_cnt, cnt)
    if max_cnt >= m:
        return True


def get_happies(grid,m):
    happies = 0
    for row in grid:
        if check_happy(row,m):
            happies += 1
    seq = [0] * n
    for col in range(n):
        column = [grid[row][col] for row in range(len(grid))]
        if check_happy(column, m):
            happies += 1
    return happies

print(get_happies(grid,m))
