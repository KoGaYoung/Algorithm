def solution(image):
    '''
    1. 왼쪽은 iterator돌면서 원본배열.extends(reverse())
    2. 아래는 iterator를 거꾸로 돌면서 .append()
    3. 방금 거꾸로돈거 부터 .extends(reverse())
    '''

    answer = [i[::] for i in image]
    for item in answer:
        reverse = [item[i] for i in range(len(item)-1, -1, -1)]
        item.extend(reverse)

    for i in range(len(image)-1, -1, -1):
        answer.append(image[i])
    # print(answer)

    for i in range(len(image), len(answer)):
        item = answer[i]
        reverse = [item[j] for j in range(len(item)-1, -1, -1)]
        answer[i].extend(reverse)
    return answer

print(solution([[207,207,207,84], [207,207,84,255], [207,84,84,207], [84,255,207,0]]))