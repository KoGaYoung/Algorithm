# n = 11
# data = '1 4'
#        '3 5'
#        '0 6'
#        '5 7'
#        '3 8'
#        '5 9'
#        '6 10'
#        '8 11'
#        '8 12'
#        '2 13'
#        '12 14'

result = 0
n = int(input())

times = []
for i in range(0, n):
    data = list(map(int, input().split()))
    data.append(data[1] - data[0])
    times.append(data)

# times.sort(key=lambda time: time[2])
#
# use = []
# for time in times:
#     flag = True
#     for i in range(time[0], time[1]):
#         if i in use:
#             flag = False
#     if flag:
#         result += 1
#         for i in range(time[0], time[1]):
#             use.append(i)

times.sort(key=lambda time: (time[1], time[0]))

result = 1
end_time = times[0][1]

for i in range(1, n):
    if times[i][0] >= end_time:
        result += 1
        end_time = times[i][1]
print(result)