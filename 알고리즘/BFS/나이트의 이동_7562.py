import sys
from collections import deque
case = int(sys.stdin.readline())

def bfs(x1, y1, x2, y2):
    q = deque()  # q = deque([x1, y1])이건 왜안되는거람
    q.append([x1, y1])
    a[x1][y1] = 1

    while q:
        x1, y1 = q.popleft()

        if x1 == x2 and y1 == y2:
            return a[x1][y1] - 1
        x_y = [[x1 - 2, y1 + 1], [x1 - 1, y1 + 2], [x1 + 1, y1 + 2], [x1 + 2, y1 + 1],
               [x1 + 2, y1 - 1], [x1 + 1, y1 - 2], [x1 - 1, y1 - 2], [x1 - 2, y1 - 1]]
        for xy_item in x_y:
            if 0 <= xy_item[0] < l and 0 <= xy_item[1] < l:
                if a[xy_item[0]][xy_item[1]] == 0:
                    q.append([xy_item[0], xy_item[1]])
                    a[xy_item[0]][xy_item[1]] = a[x1][y1] + 1

for _ in range(case):
    l = int(sys.stdin.readline())
    a = [[0]*l for _ in range(l)]
    x1, y1 = map(int, sys.stdin.readline().split())
    x2, y2 = map(int, sys.stdin.readline().split())

    if x1 == x2 and y1 == y2:
        print(0)
        continue
    else:
        print(bfs(x1, y1, x2, y2))


    # graph = {}
    #
    # for i in range(0, l):
    #     for j in range(0, l):
    #         x = [i, j]
    #
    #         y_s = [[i-1, j-1], [i-1, j], [i, j-1], [i+1, j],
    #                [i, j+1], [i+1, j+1], [i-1, j+1], [i+1, j-1]]
    #
    #         for y_item in y_s:
    #             if 0 <= y_item[0] < l and 0 <= y_item[1] < l:
    #                 y = [y_item[0], y_item[1]]
    #
    #                 if str(x) not in graph:
    #                     graph[str(x)] = [str(y)]
    #                 elif str(y) not in graph[str(x)]:
    #                     graph[str(x)].append(str(y))
    #
    #                 if str(y) not in graph:
    #                     graph[str(y)] = [str(x)]
    #                 elif str(x) not in graph[str(y)]:
    #                     graph[str(y)].append(str(x))
    #
    # root = list(map(int, sys.stdin.readline().split()))
    # target = list(map(int, sys.stdin.readline().split()))
    #
    # if root == target:
    #     print(0)
    #     break
    #
    # found = False
    # q = deque([str(root)])
    # visit = []
    #
    # while q:
    #     n = q.popleft()
    #     if n not in visit:
    #         visit.append(n)
    #         if n in graph:
    #             temp = list(set(graph[n]) - set(visit))
    #             temp.sort()
    #             q += temp









