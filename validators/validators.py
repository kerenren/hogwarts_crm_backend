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
        string_list = [self.user_dict["first_name"], self.user_dict["last_name"], self.user_dict["email"]]
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

