from collections import deque
def solution(passwords, s):
    answer = 0
    # 아파트 호, 비번 해시(딕셔너리)로
    apt_key_value = {}
    for i in passwords:
        apt_key_value[i[0]] = i[1]
    # 큐만들어주기
    q = deque([])
    s_list = s.split('#')
    del s_list[len(s_list)-1]
    for i in s_list:
        q.append(int(i))

    while q:
        item = q.popleft()
        if item in apt_key_value and len(q) >0:
            pw = q.popleft()
            if apt_key_value[item] == pw:
                answer += 1

    return answer

print(solution([[101,1234],[102,54321],[201,202],[202,1]], "101#1234#102#654321#51#203#201#202#1#"))
print(solution([[101,9999],[102,1111]], "201#9999#101#"))
print(solution([[101,9999],[102,1111]], "101#9999#102#1111#101#9999#101#9999#"))



'''

function solution(passwords, s) {
    let answer = 0;
    // 아파트 호, 비번 해시(딕셔너리)로
    let apt_key_value = {}
    passwords.forEach((i) =>{
        apt_key_value[i[0]] = i[1]
    })
    let s_list = s.split("#")
    s_list.pop()
    
    let q = s_list.map(i => {return i})
    while (q.length != 0){
        let item = q.shift();
        
        if (item in apt_key_value && q.length >0){
            if (apt_key_value[item] == q.shift()) answer +=1 
        }
    }
    return answer;
}

'''