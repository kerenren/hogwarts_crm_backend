from user.wizard import Wizard
from datetime import datetime
from magic_skill.desired_skill import DesiredSkill
from magic_skill.existing_skill import ExistingSkill
import json


class Student(Wizard):
    def __init__(self, id, first_name, last_name, email, password):
        super().__init__(id, first_name, last_name, email, password)
        self.creation_time = datetime.now()
        self.last_updated_time = ""
        self.existing_magic_skills = {}
        self.desired_magic_skills = {}

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

    def add_existing_skill(self, skill_name, level_value):
        # to do : validate skills level should be 1-5, name string length > 0
        existing_skill = ExistingSkill(skill_name)
        existing_skill.set_level(level_value)
        self.existing_magic_skills.update(existing_skill.__dict__)

    def get_desired_skills(self):
        # to do : validate skills dict if it's empty
        return self.desired_magic_skills

    def add_desired_skill(self, skill_name, level_value):
        # to do : validate skills level should be 1-5, name string length > 0
        desired_skill = DesiredSkill(skill_name)
        desired_skill.set_level(level_value)
        self.desired_magic_skills.update(desired_skill.__dict__)
