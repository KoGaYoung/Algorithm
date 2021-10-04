def solution(n, edges):
    '''
    연결을 끊어서 얻을 수 있는 최소감염 컴퓨터대수 -> 그리디
    한시간마다 한 계층씩 이동가능 -> 너비우선탐색 dfs

    deque로 너비우선탐색 순회하면서 연결된 노드 중 가장 큰 노드 하나씩 제거
    visit한 컴퓨터 대수 리턴
    '''
    tree = {}
    for item in edges:
        n1, n2 = item
        if n1 not in tree:
            tree[n1] = [n2]
        else:
            tree[n1].append(n2)

        if n2 not in tree:
            tree[n2] = [n1]
        else:
            tree[n2].append(n1)
    from collections import deque
    q = deque()
    q.append(set(tree[0]))
    visit = [0]

    while q:
        nodes = q.popleft()
        if nodes not in visit:
            visit.append(nodes)
            print(set)
            # if nodes in tree:
            #     temp = list(set(tree(nodes) - set(visit)))
            #     temp.sort()
            #     q.append(temp)

    print(visit)
    answer = 0
    return answer