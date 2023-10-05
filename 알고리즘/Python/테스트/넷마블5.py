def solution(p, vs):
    import math
    '''
    viclog = {'lion' : ['super','super','hero']} # 누가 몇번이나 이겼는지 로그 기록
    score = {'lion':10} # 점수
    
    ## test1
    print(win)
    print(viclog[win])
    print('score: ' + str(score))
    print('p:     ' + str(p))
    print('--------1--------')
    
    ## test2
    print(win)
    print(viclog(win))
    print('p:     ' + str(p) + '   and c: ' + str(c))
    print(math.ceil(p/c))
    print('score:    ' + str(score))
    print(type(math.ceil(p/c)))
    '''

    viclog = {}
    score = {}
    for game in vs:
        win = game.split(':')[0]
        lose = game.split(':')[1]
        if win not in viclog:  # 처음 이긴 경우
            viclog[win] = [lose]
            score[win] = p
        else:
            viclog[win].append(lose)
            c = 0
            for loser in viclog[win]:
                if loser == lose:
                    c += 1
            score[win] += math.ceil(p/c)


    max_winners = []
    max_score = p

    ## 로직 다 작성했으나 기억안남^.^


print(solution(4, ['super:lion', 'hero:lion', 'lion:super', 'hero:lion', 'hero:lion','lion:super', 'hero:lion', 'hero:lion','super:hero','lion:hero']))


print(solution(3, ['abd:aaa', 'abd:aaa', 'abd:aaa', 'abc:aaa', 'abc:aaa','abc:aaa']))  # abc