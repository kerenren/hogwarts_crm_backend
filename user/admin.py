from user.wizard import Wizard


class Admin(Wizard):
    def __init__(self, id, first_name, last_name, email, password):
        super().__init__(id, first_name, last_name, email, password)
