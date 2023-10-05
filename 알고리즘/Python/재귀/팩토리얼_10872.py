import sys
# 재귀
def pact(n):
    if n == 0:
        return 1
    else:
        return n * pact(n-1)
if __name__ == "__main__":
    a = int(sys.stdin.readline())
    print(pact(a))
    # 동적
    # pactorial = [1, 2]
    # for i in range(3, a+1):
    #     pactorial.append(pactorial[i-2] * i)
    #
    # pactorial[a-1]

