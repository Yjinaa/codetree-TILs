times = list(map(int, input().split()))

hour, mins, hour_, mins_ = times
start = hour * 60 + mins
end = hour_*60 + mins_

print(end - start)