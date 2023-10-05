# 10 4200
# 1
# 5
# 10
# 50
# 100
# 500
# 1000
# 5000
# 10000
# 50000
n, k = map(int, input().split())

coins =list(int(input()) for _ in range(n))

count = 0
for i in range(n, 0, -1):
    count += k // coins[i-1]
    k %= coins[i-1]
print(count)
