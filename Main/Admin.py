class Admin:
    password: str

    def __init__(self, password):
        self.password = password

    def set_password(self):
        self.password = "password"

    def get_password(self):
        return self.password
