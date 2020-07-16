from magic_skill.skill import Skill


class DesiredSkill(Skill):
    def __init__(self, name):
        super().__init__(name)
        self.level = None

    def set_level(self, value):
        self.level = value

    def get_level(self):
        return self.level
