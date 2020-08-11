import pymongo
from user.student import Student


class MongoDataLayer:
    def __create(self):
        self.__client = pymongo.MongoClient("localhost", 27017)
        self.__db = self.__client["hogwarts_crm"]
        self.__students_collection = self.__db["students"]

    def __init__(self):
        self.__create()

    def is_email_existing(self, student_dict):
        if self.__students_collection.find_one({"email": {'$in': [student_dict["email"]]}}):
            return True
        else:
            return False

    def get_all_students(self):
        students_list = []
        students = self.__students_collection.find()
        for student in students:
            student.pop("_id")
            students_list.append(student)
        return students_list

    def add_student(self, student_dict):
        if self.is_email_existing(student_dict):
            raise ValueError("Email already exists!")

        response = self.__students_collection.insert_one(student_dict)
        output = {'Status': 'Successfully inserted!',
                  'Student_ID': str(response.inserted_id)}
        return output

    def remove_student(self, student_dict):
        if self.is_email_existing(student_dict):
            response = self.__students_collection.delete_one({"email": student_dict["email"]})
            output = {'Status': 'Successfully Deleted' if response.deleted_count > 0 else "Student not found."}
            return output

    def get_student(self, student_email):
        student_dict = self.__students_collection.find_one({"email": {'$in': [student_email]}})
        if not student_dict:
            raise ValueError("Student not found")
        if not self.__db.find():
            raise ValueError("database students collection is empty")
        if len(student_email) == 0:
            raise ValueError("students_email is missing")
        if type(student_email) != str:
            raise ValueError("students_email should be a string")

        student_instance = Student.from_json(student_dict)
        return student_instance

    def edit_student(self, updated_student_dict, student_email):
        if not self.is_email_existing(updated_student_dict):
            raise ValueError("Student email is not registered")
        response = self.__students_collection.update({'email': student_email}, {'$set': updated_student_dict})
        print(response)
        output = {'Status': "Successfully Updated student's profile" if response['nModified'] > 0 else "Nothing was updated."}
        return output
