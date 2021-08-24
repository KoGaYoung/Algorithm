
# if __name__ == "__main__":
h, m = map(int, input().split())
minus_m = m - 45
if minus_m < 0:
    if h == 0:
        h = 23
    else:
        h -= 1
    minus_m += 60

print(str(h) + ' ' + str(minus_m))


