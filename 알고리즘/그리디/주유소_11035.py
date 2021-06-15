# 4
# 2 3 1
# 5 2 4 1
N = int(input())
s1 = input()
s2 = input()
costs = list(map(int, s1.split()))
spot = list(map(int, s2.split()))

total_cost = 0
m = spot[0]
total_cost += costs[0] * m

for p in range(1, N-1):
    if spot[p] < m:
        total_cost += costs[p] * spot[p]
        m = spot[p]
    else:
        total_cost += costs[p] * m

print(total_cost)