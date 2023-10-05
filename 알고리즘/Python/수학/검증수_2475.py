import sys
# if __name__ == "__main__":
a = list(map(int, sys.stdin.readline().split()))
a = [i ** 2 for i in a]
print(sum(a)%10)