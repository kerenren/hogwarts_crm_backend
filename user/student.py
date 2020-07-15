from user.wizard import Wizard
from datetime import datetime
import json


class Student(Wizard):
    def __init__(self, id, first_name, last_name, email, password, existing_magic_skills={}, desired_magic_skills={}):
        super().__init__(id, first_name, last_name, email, password)
        self.creation_time = datetime.now()
        self.last_updated_time = ""
        self.existing_magic_skills = existing_magic_skills
        self.desired_magic_skills = desired_magic_skills

    def __str__(self):
        # existing_magic_skills = {}
        # desired_magic_skills = {}
        # for skill in self.existing_magic_skills:
        #     existing_magic_skills += skill.__str__()
        # for skill in self.existing_magic_skills:
        #     desired_magic_skills += skill.__str__()
        student_json = json.dumps(self, default=lambda o: o.__dict__())
        return student_json

    def get_existing_skills(self):
        # to do : validate skills dict if it's empty
        return self.existing_magic_skills

    def add_existing_skill(self, skill_name, level):
        # to do : validate skills level should be 1-5, name string length > 0
        self.existing_magic_skills.update({skill_name: level})

    def get_desired_skills(self):
        # to do : validate skills dict if it's empty
        return self.desired_magic_skills

    def add_desired_skill(self, skill_name, level):
        # to do : validate skills level should be 1-5, name string length > 0
        self.desired_magic_skills.update({skill_name: level})
