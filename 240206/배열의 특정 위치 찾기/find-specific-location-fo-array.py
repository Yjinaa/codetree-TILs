nums = list(map(int, input().split()))

evens = sum(nums[1::2])
threes = sum(nums[2::3]) / len(nums[2::3])

print(f'{evens} {threes:.1f}')