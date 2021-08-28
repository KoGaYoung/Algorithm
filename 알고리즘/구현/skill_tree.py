'''

롤 플레잉 vedio 게임에서 플레이어는 세계를 탐험하고 퀘스트를 완료하고 새로운 기술을 배우는 가상의 캐릭터의 역할을 맡습니다.
스킬 트리는 캐릭터의 성장을 진행하기 위한 시스템 중 하나입니다.
그것은 기술의 계층 구조를 나타냅니다.

이러한 시스템의 주요 어려움은 플레이어가 특정 새 기술을 배우고 싶을 때마다 먼저 배워야 하는 또 다른 기술이 있다는 것입니다.
이 규칙의 예외는 전제 조건이 없기 때문에 게임에서 가장 배우기 쉬운 기술입니다.
"스킬 트리"라는 이름은 이러한 종속성이 가장 쉬운 기술이 루트에 있는 트리 구조를 생성한다는 사실에서 파생됩니다.

한 번 배운 스킬은 캐릭터가 항상 가지고 있기 때문에 다른 스킬이 필요로 하는 경우 다시 배울 필요가 없습니다.
예를 들어, 기술 1에 기술 0이 필요하고 기술 2에 기술 1이 필요하고 기술 3에 기술 1이 필요한 경우 기술 2를 배우기 위해 플레이어는 3개의 기술 2, 1 및 0을 배워야 합니다.
3을 배우면 전제 조건인 기술 1과 0이 이미 충족되었으므로 기술 3만 더 배우면 됩니다.

아래 그림에서 빨간색은 배워야 할 기술을 나타내고, 실선과 꼭짓점은 빨간색을 잠금 해제하기 위해 배워야 하는 것, 점선과 꼭짓점은 건너뛸 수 있는 것입니다.


스킬 트리를 나타내는 N 정수의 배열 T가 제공됩니다.
K번째 스킬은 T[K]번째 스킬을 이미 학습한 경우에만 배울 수 있습니다.
스킬 0은 루트이고 T[0]입니다. 위에서 설명한 예의 경우: T[0]=0, T[1] = 0, T[2] = 1, T[3] = 1, 따라서 T = [0,0,1,1]입니다.

'''

from collections import deque


def dfs_stack(graph, r, a):
    visit = []
    s = [r]

    while s:
        n = s.pop()
        if n == a:
            visit.append(n)
            return visit
        if n not in visit:
            visit.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visit))
                temp.sort(reverse=True)
                s += temp
    return visit

def solution(T, A):
    # write your code in Python 3.6
    graph = {}
    for n1, n2 in enumerate(T):
        if n1 not in graph:
            graph[n1] = [n2]
        elif n2 not in graph[n1]:
            graph[n1].append(n2)

        if n2 not in graph:
            graph[n2] = [n1]
        elif n1 not in graph[n2]:
            graph[n2].append(n1)

    v = []
    for aa in A:
        v.extend(dfs_stack(graph, 0, aa))

    v = set(v)
    return len(v)

# print(solution([0, 0, 1, 1], [2]))  # return 3  # 0, 1, 3
#
print(solution([0, 0, 0, 0, 2, 3, 3], [2, 5, 6]))  # return 5 # 0 2 3 5 6
#
# print(solution([0, 0, 1, 2], [1, 2]))  # return 3 # 0 1 2
#
# print(solution([0, 3, 0, 0, 5, 0, 5], [4, 2, 6, 1 ,0]))  # return 5 # 0 2 3 5 6


