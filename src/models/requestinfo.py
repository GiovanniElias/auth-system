class RequestInfo:
    
    def __init__(self, info:dict) -> None:
        self.email = info.get('email')
        self.password = info.get('password')
        if 'confirm_password' in info.keys():
            self.confirm_password = info.get('confirm_password')

    def properties(self):
        return [k for k in self.__dict__]
