from collections import deque

com = int(input())
net = int(input())

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

graph = {}
for i in range(net):
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


print(len(bfs_deque(graph, 1))-1)