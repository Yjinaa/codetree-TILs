from collections import Counter
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Write your code here!

def get_happies(grid):
    happies = 0
    for i in range(2):
        for row in range(n):
            nums = []
            for col in range(n):
                nums.append(grid[row][col])
            cnt = Counter(nums)
            if m in cnt.values():
                happies += 1
        grid = list(map(list, zip(*grid)))
    return happies


print(get_happies(grid))