# n, m, k = 5, 8, 3
# array = '2 4 5 3 6'

n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort(reverse=True)

f_big = data[0]
s_big = data[1]

result = 0

# for i in range(1, m + 1):
#     if i % k == 0:
#         result += s_big
#     else:
#         result += f_big

'''
더할때마다 m-1, m이 0이 되면 탈출
가장 큰 수를 k번 더하고 두번째로 큰 수를 한번 더하기 
'''
# while True:
#     for i in range(0, k):
#         if m == 0:
#             break
#         result += f_big
#         m -= 1
#     if m == 0:
#         break
#     result += s_big
#     m -= 1

'''
수열의 길이 반복제한길이의+1(=k+1)
큰 수가 더해지는 횟수
작은 수가 더해지는 횟수
'''
count = k * int(m / (k+1))
count += m % (k+1)

result = f_big * count + s_big * (m - count)

print(result)


