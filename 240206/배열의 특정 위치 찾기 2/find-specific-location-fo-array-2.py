nums = list(map(int, input().split()))

evens = sum(nums[1::2])
odds = sum(nums[0::2])

if evens >= odds:
    print(evens - odds)
else:
    print(odds-evens)