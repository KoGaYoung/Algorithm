# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
from collections import deque
import sys

def bfs_deque(graph, r):
    visit = []

    q = deque([r])

    while q:
        n = q.popleft()
        if n not in visit:
            visit.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visit))
                temp.sort()
                q += temp

    return visit

def dfs_stack(graph, r):
    visit = []
    s = [r]

    while s:
        n = s.pop()
        if n not in visit:
            visit.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visit))
                temp.sort(reverse=True)
                s += temp
    return visit

n, m, r = map(int, sys.stdin.readline().split())

graph = {}
for i in range(m):
    edge_info = input().split(' ')
    n1, n2 = [int(j) for j in edge_info]
    if n1 not in graph:
        graph[n1] = [n2]
    elif n2 not in graph[n1]:
        graph[n1].append(n2)

    if n2 not in graph:
        graph[n2] = [n1]
    elif n1 not in graph[n2]:
        graph[n2].append(n1)

print(" ".join(str(i) for i in dfs_stack(graph, r)))
print(" ".join(str(i) for i in bfs_deque(graph, r)))
