import sys

if __name__ == "__main__":
    ''' 
    문자열 길이순 정렬 후 최빈값을 배열에 저장
    '''
    n = int(sys.stdin.readline())
    word = [sys.stdin.readline() for _ in range(n)]

    word.sort(key=len, reverse=True)
    w_c = [[] for _ in word[0]]

    for w in word:
        for i, ch in enumerate(w):
            w_c[i].append(ch)

    from collections import Counter

