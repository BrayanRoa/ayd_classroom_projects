class RoleDTO:
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self):
        return {"name": self.name}
