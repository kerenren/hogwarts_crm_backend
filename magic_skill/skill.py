import json


class Skill:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        skill_json_string = json.dumps(self.__dict__)
        return skill_json_string
