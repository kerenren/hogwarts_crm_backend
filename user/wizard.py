import json
from datetime import datetime


class Wizard:

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.creation_time = ""
        self.last_updated_time = ""

    def __str__(self):
        person_json = json.dumps(self, default=lambda obj: obj.__dict__)
        return person_json

    def get_email(self):
        return self.email

    def update_first_name(self, new_first_name):
        self.first_name = new_first_name
        self.last_updated_time = datetime.now().strftime("%m-%d-%y %H:%I:%S")

    def update_last_name(self, new_last_name):
        self.last_name = new_last_name
        self.last_updated_time = datetime.now().strftime("%m-%d-%y %H:%I:%S")
