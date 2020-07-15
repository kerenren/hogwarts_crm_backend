import json


class Wizard:

    def __init__(self, id, first_name, last_name, email, password):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.creation_time = ""
        self.last_updated_time = ""

    def __str__(self):
        person_json = json.dumps(self, default=lambda obj: obj.__dict__)
        return person_json
