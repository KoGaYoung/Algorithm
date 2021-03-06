def solution(a, b, g, s, w, t):
    '''
    a - 필요한 금
    b - 필요한 은
    g - 도시별 갖고있는 금
    s - 도시별 갖고있는 은
    w - 한번에 운반가능한 량
    t - 한번에 걸리는 시간

    그리디 a, b를 없애야함

    도시가 3개이고, 0번과 1번 도시는 금만 70kg씩 가지고 있고 2번 도시는 은을 500kg 가지고 있습니다.
    0번 도시의 트럭은 용량은 100kg, 편도 완주 시간은 4시간입니다.
    1번 도시의 트럭은 용량은 100kg, 편도 완주 시간은 8시간입니다.
    2번 도시의 트럭은 용량은 2kg, 편도 완주 시간은 1시간입니다.
    금은 0번 도시의 트럭과 1번 도시의 트럭이 각각 45kg씩 나누어서 운반하면 8시간 안에 필요한 모든 금을 조달할 수 있습니다.
    은은 2번 도시의 트럭이 한 번에 2kg씩 250번 운반하면(249번 왕복 + 1번 편도) 총 499시간 만에 필요한 모든 은을 조달할 수 있습니다.
    따라서, 499를 return 해야 합니다.

    '''
    count = 0
    if len(g) == 1:
        sum = a+b
        while sum > 0:
            if sum - w[0] > 0:
                sum -= w[0]
                count += t[0] * 2
            else:
                sum -= w[0]
                count += t[0]
    else:
        pass
    return count


print(solution(10, 10, [100], [100], [7], [10]))
print(solution(90, 500, [70,70,0], [0,0,500], [100,100,2], [4,8,1]))
