def selfnum(n, check):
    result = n

    while(n != 0):
        result += n % 10
        n = int(n / 10)

    if result <= 10000:
        check[result-1] = False



if __name__ == "__main__":
    check = [True for i in range(0, 10000)]
    for n in range(1, 10001):
        selfnum(n, check)

    for i, n in enumerate(check):
        if n:
            print(i+1)


