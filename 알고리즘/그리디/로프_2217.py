n = int(input())
lope = list(int(input()) for _ in range(n))

lope.sort()
print(lope[0]* n)