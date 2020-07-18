from user.wizard import Wizard
from datetime import datetime
from magic_skill.desired_skill import DesiredSkill
from magic_skill.existing_skill import ExistingSkill
import json


class Student(Wizard):
    def __init__(self, id, first_name, last_name, email, password, existing_magic_skills=[], desired_magic_skills=[]):
        super().__init__(id, first_name, last_name, email, password)
        self.creation_time = datetime.now().strftime("%m-%d-%y")
        self.last_updated_time = ""
        self.existing_magic_skills = existing_magic_skills
        self.desired_magic_skills = desired_magic_skills

    def __str__(self):
        student_json = json.dumps(self.__dict__, default=lambda o: o.__dict__())
        return student_json

    # converts user from json to Student
    @staticmethod
    def from_json(student_dict):
        new_student = Student(student_dict["id"], student_dict["first_name"], student_dict["last_name"],
                              student_dict["email"], student_dict["password"], student_dict["existing_magic_skills"],
                              student_dict["desired_magic_skills"])
        print(f'The new student account {student_dict["email"]} has been created ')
        return new_student

    def get_existing_skills(self):
        # todo : validate skills dict if it's empty
        return self.existing_magic_skills

    def add_existing_skill(self, skill_name, level_value):
        # todo : validate skills level should be 1-5, name string length > 0
        existing_skill = ExistingSkill(skill_name)
        existing_skill.set_level(level_value)
        self.existing_magic_skills.append(existing_skill.__dict__)
        self.last_updated_time = datetime.now().strftime("%m-%d-%y")

    def get_desired_skills(self):
        # todo : validate skills dict if it's empty
        return self.desired_magic_skills

    def add_desired_skill(self, skill_name, level_value):
        # todo : validate skills level should be 1-5, name string length > 0
        desired_skill = DesiredSkill(skill_name)
        desired_skill.set_level(level_value)
        self.desired_magic_skills.append(desired_skill.__dict__)
        self.last_updated_time = datetime.now().strftime("%m-%d-%y")

# student = Student("er4", "Harry", "Potter", "potter@hogwartsedu.com", "nnnn")
# student.add_desired_skill("invisible", 1)
# student.add_desired_skill("fly", 5)
# student.add_existing_skill("expanding", 5)
# print(student.__str__())
# print(type(student))
#
# # load json string into python object
# student2 = Student.from_json(
#     '{"id": "er4", "first_name": "Hermione", "last_name": "Granger", "email": "hermione@hogwartsedu.com", "password": "nnnn", "creation_time": "07-16-20", "last_updated_time": "", "existing_magic_skills": [{"name": "expanding", "level": 5}], "desired_magic_skills": [{"name": "invisible", "level": 1}, {"name": "fly", "level": 5}]}')
# print(student2)
