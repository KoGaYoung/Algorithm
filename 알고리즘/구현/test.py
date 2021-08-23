class solution_cls():
    def user_login(self, user_id, password, infos):
        if self.login == 0:
            for info in infos:
                info = info.split(' ')
                if user_id == info[0] and password == info[1]:
                    self.login = 1
                    return True
        return False

    def user_add(self):
        if self.login == 0:
            return False
        else:
            return True
    def user_order(self):
        if self.login == 1 and self.order == 0:
            self.order = 1
            return True
        else:
            return False
    def __init__(self, *args):
        self.login , self.order = 0, 0
        self.check = False
        self.answer = []

        for action in actions:
            act = action.split(' ')
            if act[0] == 'LOGIN':
                check = self.user_login(act[1], act[2], infos)
            elif act[0] == 'ADD':
                check = self.user_add()
            else:
                check = self.user_order()
            self.answer.append(check)

def solution(infos, actions):
    cls = solution_cls(infos, actions)
    return cls.answer