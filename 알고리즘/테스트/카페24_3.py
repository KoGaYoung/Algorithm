'''


주어진 둘레의 길이로 만들 수 있는 삼각형의 개수를 구하는 프로그램을 작성하십시오.

예를 들어 삼각형의 둘레의 길이가 9m라고 하면,

한 변의 길이가 1m, 두 변의 길이가 4m인 삼각형

한 변의 길이가 2m, 다른 변의 길이가 3m, 나머지 변의 길이가 4m인 삼각형

세 변의 길이가 모두 3m인 삼각형

총 3가지 삼각형을 만들 수 있습니다.

입력 : 삼각형 둘레의 길이( 1이상 100이하 )

출력 : 만들어질 수 있는 서로 다른 삼각형의 수

'''

def solution(size):
    answer = 0
    for a in range(1, size):
        for b in range(a, size):
            c = size-(a+b)
            if c < b:
                break  # 중복제외
            if (b+a) > c:
                answer+=1  # 삼각형 성립하는지

    return answer