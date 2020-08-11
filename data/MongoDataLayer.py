import pymongo


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
        if self.is_email_existing(student_dict) is True:
            raise ValueError("Email already exists!")

        response = self.__students_collection.insert_one(student_dict)
        output = {'Status': 'Successfully inserted!',
                  'Student_ID': str(response.inserted_id)}
        return output

    def remove_student(self, student_dict):
        if self.is_email_existing(student_dict) is True:
            response = self.__students_collection.delete_one({"email": student_dict["email"]})
            output = {'Status': 'Successfully Deleted' if response.deleted_count > 0 else "Student not found."}
            return output
