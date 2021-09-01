
import sys

if __name__ == "__main__":

    a = int(sys.stdin.readline())
    li = [int(sys.stdin.readline()) for _ in range(a)]

    '''
    첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
    '''
    print(round(sum(li)/len(li)))

    '''
    둘째 줄에는 중앙값을 출력한다.
    '''
    li.sort()
    if len(li) % 2 == 0:
        print( (li[int(len(li)/2) - 1] + li[int(len(li)/2)]) / 2 )
    else:
        print(li[int(len(li)/2)])

    '''
    셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
    '''
    dic = {}
    for item in li:
        if str(item) not in dic.keys():
            dic[str(item)] = 1
        else:
            dic[str(item)] += 1
    re = []
    for key in dic.keys():
        if dic[key] == max(dic.values()):
            re.append(int(key))
    re.sort()
    print(re[0] if len(re) == 1 else re[1])
    '''
    넷째 줄에는 범위를 출력한다.
    '''
    print(max(li) - min(li))