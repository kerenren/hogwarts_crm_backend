from magic_skill.skill import Skill


class ExistingSkill(Skill):
    def __init__(self, name):
        super().__init__(name)
        self.level = None

    def set_level(self, value):
        self.level = value

    def get_level(self):
        return self.level


# skill = ExistingSkill("fly")
# skill.set_level(2)
# print(type(skill.__dict__))
# print(skill.__str__())
# self note: ExistingSkill inherited .__str__() from Skill
