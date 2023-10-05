def solution(queries):
    '''
    배열을 반씩 잘라서 홀수는 중간원소 빼기
    비교해가며 앞배열과 뒷배열의 원소가 똑같아질 때까지 뺴야함
    각 col별로 최소값이 될 때까지 빼는 것.
    '''
    answer = []
    for turn in queries:
        f = turn[:int(len(turn)/2)]
        b = turn[int(len(turn)/2) if len(turn) % 2 == 0 else int(len(turn)/2)+1:]

        if f == b:  # f:[0,1] b:[0,1]
            answer.append(0)
        else:
            c_minus = 0
            for i in range(0, len(f)):
                c_minus += abs(f[i] - b[i])
            if c_minus % 2 == 0:
                answer.append(0)
            else:
                answer.append(1)
    return answer

print(solution([[2,0], [3,1]]))  # [0,0]

print(solution([[1,4,3], [1,2,2]]))  # [0,1]

print(solution([[0,2,0,1], [0,1,0,1]]))  # [1,0]

