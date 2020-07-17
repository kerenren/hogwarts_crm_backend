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

    # receiving all students within the dictionary.
    def get_all_students(self):
        return self.__students

    def convert_students_to_json_str(self):
        all_students_dict = self.get_all_students()
        student_json_str = json.dumps(all_students_dict, default=lambda o: o.__dict__, indent=4)
        return student_json_str

    # persisting all the students' class instances in the dictionary into a json file called students.json
    def persist_students(self):
        #  create path to json file
        folder_where_json_file_is = pathlib.Path(__file__).parent
        db_file = str(folder_where_json_file_is) + os.sep + "students.json"

        # check if json file exist
        if os.path.exists(db_file):
            os.remove(db_file)
        else:
            raise Exception("students.json file doesn't exist")

        students_json = self.convert_students_to_json_str()

        with open("students.json", "a") as write_file:
            write_file.write(students_json)
            return "Persist is succeed"

    # loading the data from students.json, converting it to students class instances and populating the instances
    # into the students dictionary object of the DataLayer class.
    def load_all_students(self):
        folder_where_json_file_is = pathlib.Path(__file__).parent
        read_file = str(folder_where_json_file_is) + os.sep + "students.json"

        if os.path.exists(read_file):
            with open("students.json", "r") as read_file:
                self.__students = json.load(read_file)
            return self.__students
        else:
            raise Exception("student.json file doesn't exist")


# for testing:
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
