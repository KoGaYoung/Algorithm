class user():
    def __init__(self, infos):
        self.user_info = infos
        self.login = False
        self.cart = []

    def inlogin(self, id_pw):
        if not self.login:
            if id_pw in self.user_info:
                self.login = True  # 아이디, 비번 일치 = 로그인
                return True
            else:
                return False
        else:  # 기 로그인
            return False
    def add(self, item):
        if self.login:
            self.cart.append(item)  # 로그인 되어있으면 카트에담는다
            return True
        else:
            return False
    def order(self):
        if self.cart:
            self.cart = []
            return True
        else:
            return False





def solution(infos, actions):
    answer = []

    user1 = user(infos)

    for item in actions:
        item_list = item.split()
        if item_list[0] == 'LOGIN':
            answer.append(user1.inlogin(' '.join(item_list[1:])))
        elif item_list[0] == 'ADD':
            answer.append(user1.add(item_list[1]))
        elif item_list[0] == 'ORDER':
            answer.append(user1.order())

    return answer

print(solution(["kim password", "lee abc"], [
    "ADD 30",
    "LOGIN kim abc",
    "LOGIN lee password",
    "LOGIN kim password",
    "LOGIN kim password",
    "LOGIN lee abc",
    "ADD 30",
    "ORDER",
    "ORDER",
    "ADD 40",
    "ADD 50"
]
))

print(solution(["kim password", "lee abc"], [
    "LOGIN lee abc",
    "LOGIN kim password"
]
))