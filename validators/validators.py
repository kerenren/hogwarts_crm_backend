class Validators:
    def __init__(self, user_dict):
        self.user_dict = user_dict
        # string_type = [user_dict["id"],user_dict["first_name"],user_dict["last_name"],user_dict["email"],user_dict["password"]]

    # when we create a user, the user_dict is coming from POST response json, thus the value of num should be num not string of num
    def valid_skill_dict_value(self, skill):
        skills__list = self.user_dict[skill]
        if len(skills__list) != 0:
            for skill in skills__list:
                if type(skill["name"]) != str:
                    raise ValueError("Sorry, the skill name should be string")
                if type(skill["level"]) != int:
                    raise ValueError("Sorry, the skill level should be a number")

    def valid_user_fields_type(self):
        print(self.user_dict)
        string_list = [self.user_dict["id"], self.user_dict["first_name"], self.user_dict["last_name"],
                       self.user_dict["password"], self.user_dict["email"], self.user_dict["password"]]
        for item in string_list:
            if type(item) != str:
                raise ValueError("you fields is not a string")
        self.valid_skill_dict_value("existing_magic_skills")
        self.valid_skill_dict_value("desired_magic_skills")

    def valid_user_fields_exist(self):
        for value in self.user_dict.values():
            if not value:
                raise ValueError("missing value")

    # selfenote: if user exist in all users dict, it should return True, else it's None.
    def valid_user_exist(self, all_users):
        for k, v in all_users.items():
            if isinstance(v, dict):
                if self.user_dict["email"] in v.values():
                    return True
            return None

    def valid_user_credential(self, all_users):
        for k, v in all_users.items():
            if isinstance(v, dict):
                if v["email"] == self.user_dict["email"] and v["password"] == self.user_dict["password"]:
                    return True
                else:
                    return False
# hermione_dict = {
#     "id": "er4",
#     "first_name": "Hermione",
#     "last_name": "Granger",
#     "email": "hermione@hogwartsedu.com",
#     "password": "nnnn",
#     "creation_time": "07-16-20",
#     "last_updated_time": "rt",
#     "existing_magic_skills": [
#         {"name": "expanding",
#          "level": 5}
#     ],
#     "desired_magic_skills": [
#         {"name": "invisible", "level": 1},
#         {"name": "fly", "level": 5}
#     ]}
#
# all_user = {
#     "ishk234": {
#         "id": "er4",
#         "first_name": "Hermione",
#         "last_name": "Granger",
#         "email": "hermione@hogwartsedu.com",
#         "password": "nnnn",
#         "creation_time": "07-17-20",
#         "last_updated_time": "rt",
#         "existing_magic_skills": [
#             {"name": "expanding",
#              "level": 5}
#         ],
#         "desired_magic_skills": [
#             {"name": "invisible", "level": 1},
#             {"name": "fly", "level": 5}
#         ]},
#     "edft4d": {
#         "id": "er4",
#         "first_name": "Harry",
#         "last_name": "potter",
#         "email": "potter@hogwartsedu.com",
#         "password": "nnnn",
#         "creation_time": "07-16-20",
#         "last_updated_time": "07-17-20",
#         "existing_magic_skills": [
#             {"name": "expanding",
#              "level": 5}
#         ],
#         "desired_magic_skills": [
#             {"name": "invisible", "level": 1},
#             {"name": "fly", "level": 5}
#         ]}
# }

# validator = Validators(hermione_dict)
# validator.valid_user_fields_type()
# validator.valid_user_fields_exist()
# is_exist = validator.valid_user_exist(all_user)
# print(is_exist)
