class BaseDataLayer:
    def __init__(self):
        pass

    # setting and getting a specific student from the dictionary by its email.
    def add_student(self, student_dict):
        pass

    def remove_student(self, student_dict):
        pass

    # getting a specific student instance from the dictionary by its email.
    def get_student(self, student_email):
        pass

    def count_desired_skill_popularity(self):
        pass

    def count_existing_skill_popularity(self):
        pass

    #  get added students per day of the year
    def get_students_per_day(self, creation_time):
        pass

    # receiving all students within the dictionary.
    def get_all_students(self):
        pass

    def sign_up(self, admin_dict):
        pass

    def log_in(self, admin_credential):
        pass

    def edit_student(self, updated_student_dict, student_email):
        pass
