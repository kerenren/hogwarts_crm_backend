import pymongo


class MongoDataLayer:
    def __create(self):
        self.__client = pymongo.MongoClient("localhost", 27017)
        self.__db = self.__client["hogwarts_crm"]
        self.__students_collection = self.__db["students"]

    def __init__(self):
        self.__create()

    def get_all_students(self):
        students_list = []
        students = self.__students_collection.find()
        for student in students:
            student.pop("_id")
            students_list.append(student)
        return students_list

    def add_student(self, student_dict):
        if self.__students_collection.find_one({"email": {'$in': [student_dict["email"]]}}):
            raise ValueError("Email already exists!")

        response = self.__students_collection.insert_one(student_dict)
        output = {'Status': 'Successfully inserted!',
                  'Student_ID': str(response.inserted_id)}
        return output
