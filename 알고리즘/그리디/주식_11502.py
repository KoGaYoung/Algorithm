import sys

if __name__ == "__main__":
    '''
    - 잘못된 접근: 주가가 떨어지는 시점에 기존 구입했던 주식 판매 (Greedy)
    - 올바른 접근: 주가가 떨어지는 시점이 아니라, 현재 주가를 현재일 이후에 가장 비싸게 팔 수 있는 날에 판매
    
    값이 작아지는 시점은 그때마다 최댓값 - a[i]를 최대이익에 합해주면 됩니다
1
7
1 2 3 4 2 1 1

    맨 처음 최댓값을 1로 갱신
    그 다음 탐색에서 1을 발견. 같은 경우는 사고팔고 의미가 없으므로
    그 다음 탐색으로 넘어가서 2를 발견 최댓값을 2로 갱신
    그 다음 탐색에서 4를 발견 최댓값을 4로 갱신
    이후 3 2 1 은 계속 작아지므로
    그 말인즉슨 4보다 작으니까 계속 사뒀다가 4에서 파는게 이익이라는 뜻이므로
    최대이익+=(4-3)+(4-2)+(4-1)
    따라서 총 최대이익은 6

    '''
    t = int(sys.stdin.readline())
    for _ in range(0, t):
        t_d = int(sys.stdin.readline())
        stocks = list(map(int, sys.stdin.readline().split()))

        result = 0
        max_stock = stocks[-1]

        for i in range(len(stocks) - 1, -1, -1):
            if stocks[i] > max_stock:
                max_stock = stocks[i]
            else:
                result += max_stock - stocks[i]
        print(result)
