from validators.validators import Validators
import os, pathlib, json
from user.student import Student
from data.MongoDataLayer import MongoDataLayer


# The DataLayer class will have a dictionary containing the students class instances.
# each instance will be stored using its email property as the key within the dictionary.
class DataLayer:
    mongoDB = MongoDataLayer()

    def __init__(self):
        pass

    # setting and getting a specific student from the dictionary by its email.
    def add_student(self, student_dict):
        output = DataLayer.mongoDB.add_student(student_dict)
        return output

    def remove_student(self, student_dict):
        output = DataLayer.mongoDB.remove_student(student_dict)
        return output

    # getting a specific student instance from the dictionary by its email.
    def get_student(self, student_email):
        student_instance = DataLayer.mongoDB.get_student(student_email)
        return student_instance

    def extract_objs_by_value(self, value, objs):
        new_objs = {}
        for k, v in objs.items():
            if isinstance(v, dict):
                if value in v.values():
                    new_objs.update({v["email"]: v})
        return new_objs

    def count_skill(self, skill_type, skill_name):
        all_students = self.get_all_students()
        counter = 0
        for k, v in all_students.items():
            if isinstance(v, dict):
                skills_list = v[skill_type]
                duplicated_skills_list = [i["name"] for i in skills_list if i["name"] == skill_name]
                cnt = len(duplicated_skills_list)
                counter += cnt
        return counter

    #  get added students per day of the year
    def get_students_per_day(self, creation_time):
        all_students = self.get_all_students()
        students_per_day = self.extract_objs_by_value(creation_time, all_students)
        return students_per_day

    # receiving all students within the dictionary.
    def get_all_students(self):
        students_list = DataLayer.mongoDB.get_all_students()
        return students_list

    def convert_students_to_json_str(self):
        all_students_dict = self.get_all_students()
        student_json_str = json.dumps(all_students_dict, default=lambda o: o.__dict__, indent=4)
        return student_json_str

    # persisting all the students' class instances in the dictionary into a json file called students.json
    def persist_students(self):
        # find the folder obj of json file
        folder_where_json_file_is = pathlib.Path(__file__).parent
        #  create path to json file with os.separator
        db_file = str(folder_where_json_file_is) + os.sep + "students.json"

        # check if json file exist
        if os.path.exists(db_file):
            os.remove(db_file)
        else:
            raise Exception("students.json file doesn't exist")

        students_json = self.convert_students_to_json_str()

        with open(db_file, "a") as write_file:
            write_file.write(students_json)
            return "Persist is succeed"

    # loading the data from students.json, converting it to students class instances and populating the instances
    # into the students dictionary object of the DataLayer class.
    def load_all_students(self):
        folder_where_json_file_is = pathlib.Path(__file__).parent
        read_file = str(folder_where_json_file_is) + os.sep + "students.json"
        print(read_file)
        if os.path.exists(read_file):
            with open(read_file, "r") as r_file:
                self.__students = json.load(r_file)
            return self.__students
        else:
            raise Exception("student.json file doesn't exist")

    def edit_student(self, updated_student_dict, student_email):
        output = DataLayer.mongoDB.edit_student(updated_student_dict, student_email)
        return output
