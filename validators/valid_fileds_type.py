class Validator:
    def __init__(self, user_dict):
        self.user_dict = user_dict
        # string_type = [user_dict["id"],user_dict["first_name"],user_dict["last_name"],user_dict["email"],user_dict["password"]]

    def valid_fields_type(self):
        for item in self.user_dict:
            if type(item) != str:
                raise ValueError("you fields is not a string")

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
            return False




#
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
#
# validator = Validator(hermione_dict)
# validator.valid_fields_type()
# validator.valid_user_fields_exist()
# is_exist = validator.valid_user_exist(all_user)
# print(is_exist)
