import sys

if __name__ == "__main__":
    '''
    * 일단 이 문제는 배열에 저장해두려고하면 메모리 제한으로 터진다.
    그리디로 풀어야함
    -> 선이 항상 이어져 있지 않는 점을 신경써야함.
    '''
    t = int(sys.stdin.readline())
    lines = list(tuple(map(int, sys.stdin.readline().split())) for _ in range(t))
    lines.sort(key=lambda x: (x[0], x[1]))

    result = 0
    now_s, now_e = lines[0]
    del lines[0]
    for s, e in lines:
        if now_e < s:                # 현재 내 끝보다 새로운 선의 시작값이 클 경우(선이 이어져 있지 않음)
            result += now_e - now_s  # 지금까지의 값 정리
            now_s, now_e = s, e      # 새로운 선으로 swap
        now_e = max(e, now_e)        # 매번 새로운 Y 갱신
    result += now_e - now_s          # 남은 선 정리
    print(result)

