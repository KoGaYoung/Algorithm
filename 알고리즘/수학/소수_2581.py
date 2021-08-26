import sys
# 자꾸 시간초과 나서 에리토테네스 풀이 참고
M, N = map(int, sys.stdin.readline().split())
a = [False, False] + [True] * (N-1)
primes = []

for i in range(2, N+1):
    if a[i]:
        primes.append(i)
        for j in range(2 * i, N + 1, i):
            a[j] = False
primes = list(filter(lambda x: x >= M, primes))
for p in primes:
    print(p)
# def isprime(num, M):
#     if num < 2:
#         return
#     for i in range(2, num):
#         if num % i == 0:
#             return  # 소수가 아니다
#     if num >= M:
#         print(num)  # 소수이다
#
# if __name__ == "__main__":
#     M, N = map(int, sys.stdin.readline().split())
#     for i in range(M, N+1):
#         isprime(i, M)

