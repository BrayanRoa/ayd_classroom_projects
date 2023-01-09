class UserDTO:
    def __init__(self, email, role_id):
        self.email = email
        self.role_id = role_id

    def __str__(self):
        return {"email": self.email, "role_id": self.role_id}

    def __repr__(self):
        return self.__str__()
