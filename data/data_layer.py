from validators.validators import Validators
import os, pathlib, json
from user.student import Student


# The DataLayer class will have a dictionary containing the students class instances.
# each instance will be stored using its email property as the key within the dictionary.
class DataLayer:

    def __init__(self, students={}):
        self.__students = students

    # setting and getting a specific student from the dictionary by its email.
    def add_student(self, student):
        if student.get_email() in self.__students.keys():
            raise ValueError("Email already exists!")

        self.__students[student.get_email()] = student
        # the student here actually represents the student instance
        print("student has been added to data_layer students_dict:", self.__students)

    def remove_student(self, student):
        if student.get_email() not in self.__students.keys():
            raise ValueError("Email doesn't exist!")
        del self.__students[student.get_email()]
        print("student has been removed from data_layer students_dict:", self.__students)

    # getting a specific student from the dictionary by its email.
    def get_student(self, student_email):
        if student_email not in self.__students.keys():
            raise ValueError("Email doesn't exist!")

        student = self.__students[student_email]
        return student

    def extract_objs_by_value(self, value, objs):
        new_objs = {}
        for k, v in objs.items():
            if isinstance(v, dict):
                if value in v.values():
                    new_objs.update({v["email"]: v})
        return new_objs

    #  get added students per day of the year
    def get_students_per_day(self, creation_time):
        all_students = self.get_all_students()
        students_per_day = self.extract_objs_by_value(creation_time, all_students)
        return students_per_day

    # receiving all students within the dictionary.
    def get_all_students(self):
        return self.__students

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
        # folder_where_json_file_is = pathlib.Path("./data")
        read_file = str(folder_where_json_file_is) + os.sep + "students.json"
        print(read_file)
        if os.path.exists(read_file):
            with open(read_file, "r") as r_file:
                self.__students = json.load(r_file)
            return self.__students
        else:
            raise Exception("student.json file doesn't exist")

#
# # for testing:
# student = Student("er4", "Harry", "Potter", "potter@hogwartsedu.com", "nnnn")
# student.add_existing_skill("Obliviate",3)
# student.add_desired_skill("invisible", 1)
# student.add_desired_skill("fly", 5)
# student.add_existing_skill("expanding", 5)
# student2 = Student.from_json(
#     '{"id": "er4", "first_name": "Hermione", "last_name": "Granger", "email": "hermione@hogwartsedu.com", "password": "nnnn", "creation_time": "07-16-20", "last_updated_time": "", "existing_magic_skills": [{"name": "expanding", "level": 5}], "desired_magic_skills": [{"name": "invisible", "level": 1}, {"name": "fly", "level": 5}]}')
# student2.add_desired_skill("Riddikulu", 5)
# data = DataLayer()
# data.add_student(student)
# data.add_student(student2)
# # data.remove_student(student)
# student_json_str = data.convert_students_to_json_str()
# student_dict = json.loads(student_json_str)
# print(student_json_str)
# data.persist_students()
#
# data.load_all_students()
# print(data.get_all_students())
# student_2=data.get_student("hermione@hogwartsedu.com")
# print(help(student2))
