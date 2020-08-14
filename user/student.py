from user.wizard import Wizard
from datetime import datetime
from magic_skill.desired_skill import DesiredSkill
from magic_skill.existing_skill import ExistingSkill
import json


class Student(Wizard):
    def __init__(self, first_name, last_name, email, creation_time, last_updated_time, existing_magic_skills=[], desired_magic_skills=[]):
        super().__init__(first_name, last_name, email)
        self.creation_time = creation_time
        self.last_updated_time = last_updated_time
        self.existing_magic_skills = existing_magic_skills
        self.desired_magic_skills = desired_magic_skills

    def __str__(self):
        student_json = json.dumps(self.__dict__, default=lambda o: o.__dict__())
        return student_json

    # converts user from json to Student
    @staticmethod
    def from_json(student_dict):
        new_student = Student(student_dict["first_name"], student_dict["last_name"],
                              student_dict["email"], student_dict["creation_time"], student_dict["last_updated_time"], student_dict["existing_magic_skills"],
                              student_dict["desired_magic_skills"])
        print(f'The student {student_dict["email"]} has been converted from json string to the Student instance ')
        return new_student

    def get_existing_skills(self):
        # todo : validate skills dict if it's empty
        return self.existing_magic_skills

    def get_existing_skill_by_name(self, skill_name):
        for skill in self.existing_magic_skills:
            if skill["name"] == skill_name:
                return skill

    def get_desired_skill_by_name(self, skill_name):
        for skill in self.desired_magic_skills:
            if skill["name"] == skill_name:
                return skill

    def add_existing_skill(self, skill_name, level_value):
        # todo : validate skills level should be 1-5, name string length > 0
        existing_skill = ExistingSkill(skill_name)
        existing_skill.set_level(level_value)
        self.existing_magic_skills.append(existing_skill.__dict__)
        self.last_updated_time = datetime.now().strftime("%m-%d-%y %H:%I:%S")
        print(f"The existing skill {skill_name} has been added! ")

    def update_existing_skill(self, skill_name, level_value):
        # todo : validate skills level should be 1-5, name string length > 0
        existing_skill = self.get_existing_skill_by_name(skill_name)
        existing_skill["level"] = level_value
        self.last_updated_time = datetime.now().strftime("%m-%d-%y %H:%I:%S")
        print(f"The existing skill {skill_name} has been updated! ")

    def get_desired_skills(self):
        # todo : validate skills dict if it's empty
        return self.desired_magic_skills

    def add_desired_skill(self, skill_name, level_value):
        # todo : validate skills level should be 1-5, name string length > 0
        desired_skill = DesiredSkill(skill_name)
        desired_skill.set_level(level_value)
        self.desired_magic_skills.append(desired_skill.__dict__)
        self.last_updated_time = datetime.now().strftime("%m-%d-%y %H:%I:%S")
        print(f"The desired skill {skill_name} has been updated! ")

    def update_desired_skill(self, skill_name, level_value):
        # todo : validate skills level should be 1-5, name string length > 0
        desired_skill = self.get_desired_skill_by_name(skill_name)
        desired_skill["level"] = level_value
        self.last_updated_time = datetime.now().strftime("%m-%d-%y %H:%I:%S")
        print(f"The desired skill {skill_name} has been updated! ")
