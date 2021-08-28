
import sys

if __name__ == "__main__":
    '''
    첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.

    둘째 줄에는 중앙값을 출력한다.

    셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.

    넷째 줄에는 범위를 출력한다.
    '''
    a = int(sys.stdin.readline())
    li = [int(sys.stdin.readline()) for _ in range(a)]

    print(round(sum(li)/len(li)))

    li.sort()
    if len(li) % 2 == 0:
        print( (li[int(len(li)/2) - 1] + li[int(len(li)/2)]) / 2 )
    else:
        print(li[int(len(li)/2)])

    dic = {}
    for item in li:
        if item not in dic:
            dic[li] = 1
        else:
            dic[li] += 1


    print(max(li) - min(li))