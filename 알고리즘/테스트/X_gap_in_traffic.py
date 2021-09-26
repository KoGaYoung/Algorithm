#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'order' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. UNWEIGHTED_INTEGER_GRAPH city
#  2. INTEGER company
#

#
# For the unweighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i].
#
#

def order(city_nodes, city_from, city_to, company):
    from collections import deque
    # dfs (3/14)
    # print(city_nodes)
    # print(city_from)
    # print(city_to)
    graph = {}
    for i in range(0, len(city_from)):
        n1 = city_from[i]
        n2 = city_to[i]
        if n1 not in graph:
            graph[n1] = [n2]
        elif n2 not in graph[n1]:
            graph[n1].append(n2)

        if n2 not in graph:
            graph[n2] = [n1]
        elif n1 not in graph[n2]:
            graph[n2].append(n1)

    visit = []
    q = deque([company])
    while (q):
        n = q.popleft()
        if n not in visit:
            visit.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visit))
                temp.sort()
                q += temp
    return visit[1:]


if __name__ == '__main__':
    print(order(5, [1, 1, 1, 2, 3], [2, 5, 3, 4, 5], 1)) #   [2,3,5,4]
    print(order(3, [1], [2], 2))  # [1]