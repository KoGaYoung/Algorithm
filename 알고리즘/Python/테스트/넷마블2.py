def solution(stats):
    '''
    공격력, 수비력이 모두 높은 경우 먹이사슬 관계로 정의
    그 중 가장 큰 연속 횟수

    1. list를 [0],[1]순으로 정렬
    2. 연속이 끊길 떄마다 combo 배열에 넣어서 max값 구하기

    + 리스트 정렬방법 정리
    '''
    m = stats[0]
    for i in range(0, len(stats)):
        for j in range(i+1, len(stats)):
            if stats[i][0] >= stats[j][0] and stats[i][1] > stats[j][1]:
                stats[i], stats[j] = stats[j], stats[i]
                break

    # 완전탐색이구나..
    max_combo = [0]
    for i in range(len(stats)-1, -1, -1):
        combo = 1
        for j in range(i-1, -1, -1):
            if stats[i][0] > stats[j][0] and stats[i][1] > stats[j][1]:
                combo += 1
        max_combo.append(combo)
    return max(max_combo)

print(solution([[10,7], [7,10], [7,6]]))  # 2

print(solution([[3,3], [1,1], [5,5], [7,7]]))  # 4

print(solution([[1,9], [6,6], [7,7], [8,8], [8,8]]))  # 3

print(solution([[2,10], [5,9], [8,3]]))  # 1

