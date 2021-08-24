# import sys
# if __name__ == "__main__":
#     a, b, v = map(int, sys.stdin.readline().split())
#
#     n = 0
#     while (a-b) * (n-1) + a < v:
#         n += 1
#     print(n)

A, B, V = map(int,input().split())
d = (V-B)/(A-B)
print(int(d) if d == int(d) else int(d)+1)