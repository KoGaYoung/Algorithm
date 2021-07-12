# 7 392
import sys
from collections import deque
s, t = map(int, input().split())

# 최소연산, 연산을 간선으로 생각하기
q = deque([(0, s, '')])  # [거리, 값, 연산자]
visited = set([s])  # 방문한 값 기록
found = False

if s == t:
    print(0)
    sys.exit(0)

while q:
    dist, value, opers = q.popleft()
    if value > t:  # 값의 범위를 벗어나는경
        continue
    if value == t:
        print(opers)
        found = True
        break
    for oper in ('*', '+', '-','/'):
        if oper == '*':
            next_value = value * value
        elif oper == '+':
            next_value = value + value
        elif oper == '-':
            next_value = value - value
        elif oper == '/':
            next_value = 1
        if next_value not in visited:
            q.append((dist, next_value, opers+opers))
            visited.add(next_value)

if not found:
    print(-1)
