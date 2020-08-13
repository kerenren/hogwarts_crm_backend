import pymongo
from user.student import Student


class MongoDataLayer:
    def __create(self):
        self.__client = pymongo.MongoClient("localhost", 27017)
        self.__db = self.__client["hogwarts_crm"]
        self.__students_collection = self.__db["students"]
        self.__admins_collection = self.__db["admins"]

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

    def get_all_admins(self):
        admins_cursor = self.__admins_collection.aggregate([{'$project': {'_id': 0, "first_name": 1, "last_name": 1,
                                                                          "creation_time": 1, "last_updated_time": 1,
                                                                          "email": 1}}])
        admins_list = list(admins_cursor)
        return admins_list

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
        output = {
            'Status': "Successfully Updated student's profile" if response['nModified'] > 0 else "Nothing was updated."}
        return output

    def log_in(self, credential):
        email = credential['email']
        password = credential['password']
        admin_cursor = self.__admins_collection.find({'email': {'$eq': '$email', 'password': {'$eq': '$password'}}})
        if admin_cursor:
            return True
        else:
            return False

    def sign_up(self, admin_dict):
        if self.__admins_collection.find_one({"email": {'$in': [admin_dict["email"]]}}):
            raise ValueError('Admin email has already been registered')
        response = self.__admins_collection.insert_one(admin_dict)
        output = {'Status': 'Successfully registered!',
                  'Admin_ID': str(response.inserted_id)}
        return output

    def count_desired_skill_popularity(self):
        pipeline = [{"$project": {"desiredSkills": "$desired_magic_skills"}}, {"$unwind": "$desiredSkills"},
                    {"$group": {"_id": "$desiredSkills.name", "sum": {"$sum": "$desiredSkills.level"}}}]
        desired_skills_popularity = self.__students_collection.aggregate(pipeline)
        popularity = list(desired_skills_popularity)
        return popularity

    def count_existing_skill_popularity(self):
        pipeline = [{"$project": {"existingSkills": "$existing_magic_skills"}}, {"$unwind": "$existingSkills"},
                    {"$group": {"_id": "$existingSkills.name", "sum": {"$sum": "$existingSkills.level"}}}]
        existing_skills_popularity = self.__students_collection.aggregate(pipeline)
        popularity = list(existing_skills_popularity)
        return popularity

    def get_students_per_day(self, creation_time):
        pipeline = [{'$match': {'creation_time': creation_time}}, {'$count': "email"},
                    {'$group': {'_id': creation_time, 'total': {'$sum': '$email'}}}]
        cursor = self.__students_collection.aggregate(pipeline)
        total_dict = list(cursor)
        return total_dict
