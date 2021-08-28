import sys
def factorization(x):
    d = 2
    while d <= x:
        if x % d == 0:
            print(d)
            x = x / d
        else:
            d = d + 1
if __name__ == "__main__":
    a = int(sys.stdin.readline())
    factorization(a)
