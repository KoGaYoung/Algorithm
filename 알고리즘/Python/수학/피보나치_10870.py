import sys
# 재귀
# def pact(n):
#     if n == 0:
#         return 1
#     else:
#         return n * pact(n-1)
if __name__ == "__main__":
    a = int(sys.stdin.readline())
    li = [0, 1]
    if a < 2:
        print(li[a])
    else:
        for i in range(2, a+1):
            li.append(li[i-2] + li[i-1])
        print(li[a])