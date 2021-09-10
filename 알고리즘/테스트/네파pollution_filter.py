'''

한 산업체에는 N개의 공장이 있으며, 각 공장은 매달 약간의 오염물질을 생산합니다.
이 회사는 일부 공장에 하나 이상의 필터를 장착하여 총 연기 배출을 줄이기로 결정했습니다.

이러한 모든 필터는 공장의 오염을 절반으로 줄입니다.
두 번째(또는 후속) 필터를 적용하면 기존 필터를 장착한 후 배출되는 나머지 오염 물질을 다시 절반으로 줄입니다.
예를 들어, 처음에 6단위의 오염을 생산하는 공장은 하나의 필터로 3단위, 두 개의 필터로 1.5단위, 트리 필터로 0.75단위를 생성합니다.

공장에서 생성된 오염의 양을 설명하는 N 정수 배열이 제공됩니다.
당신의 임무는 오염의 총합을 적어도 절반으로 줄이는 데 필요한 최소 필터 수를 찾는 것입니다.
'''

def solution(A):
    # write your code in Python 3.6
    f_same = True
    for a in A:
        if A[0] != a:
            f_same = False

    if f_same:
        return len(A)
    else:
        count = 0
        origin_sum = sum(A)

        while origin_sum/2 < sum(A):
            A[A.index(max(A))] = max(A)/2
            count+=1
        return count


print(solution([5, 19, 8, 1]))  # 3
print(solution([10, 10]))  # 2
print(solution([3, 0, 5]))  # 2
