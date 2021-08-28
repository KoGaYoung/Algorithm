import sys
if __name__ == "__main__":
#     a = int(sys.stdin.readline())
#     b = int(sys.stdin.readline())
    a, b = map(int, sys.stdin.readline().split())
    print(a//b)
    print(a%b)
