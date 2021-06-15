# 5
# 3 1 4 3 2
n = int(input())
times = list(map(int, input().split()))

times.sort()

result = 0
time = 0
last_time = 0

for t in times:
    time = last_time + t
    result += time
    last_time = time


print(result)
