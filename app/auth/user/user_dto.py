class UserDTO():
    def __init__(self, email, password):
        self.email=email
        self.password=password
    
    def __str__(self):
        return {"email":self.email,"passwrpd":self.password}
    def __repr__(self):
        return self.__str__()