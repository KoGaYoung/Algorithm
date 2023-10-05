import sys
from collections import deque

x, y = map(int, sys.stdin.readline().split())

tomato = []
q = deque()  # 익은 토마토를 큐에 넣고시작
pre_tomato = []
for i in range(y):
    row = list(map(int, sys.stdin.readline().split()))
    tomato.append(row)
    for j in range(x):
        if row[j] == 1:
            q.append([i, j])
        elif row[j] == 0:
            pre_tomato.append(0)



if not pre_tomato:
    print(0)
else:
    max = 0
    while q:

        x1, y1 = q.popleft()

        x_y = [[x1 - 1, y1], [x1 + 1, y1], [x1, y1 - 1], [x1, y1 + 1]]
        for xy_item in x_y:
            if 0 <= xy_item[0] < y and 0 <= xy_item[1] < x and tomato[xy_item[0]][xy_item[1]] == 0:
                q.append([xy_item[0], xy_item[1]])
                tomato[xy_item[0]][xy_item[1]] = tomato[x1][y1] + 1
                max = tomato[x1][y1] + 1


    flag = False
    for t in tomato:
        if 0 in t:
            flag = True
    if flag:
        print(-1)
    else:
        print(max-1)

