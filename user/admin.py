from user.wizard import Wizard


class Admin(Wizard):
    def __init__(self, first_name, last_name, email, password):
        super().__init__(first_name, last_name, email)
        self.password = password
