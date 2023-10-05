import sys

def isprime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if(n % i == 0):
            return False
    return True

if __name__ == "__main__":
    t = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    answer = 0
    for n in a:
        if isprime(n):
            answer += 1
    print(answer)